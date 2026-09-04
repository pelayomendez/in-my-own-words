#!/usr/bin/env python3
"""Normalise a fetched page, feed or local file into sources/raw/.

Called by add-source.sh. Writes one dated Markdown file per piece and prints
the paths. Text only — no trait extraction, that is the skill's job.
"""

import argparse
import datetime
import html
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

CONTENT_NS = {"content": "http://purl.org/rss/1.0/modules/content/"}
ATOM = "{http://www.w3.org/2005/Atom}"


def slug(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]
    return s or "untitled"


def strip_html(markup: str) -> str:
    markup = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", markup)
    markup = re.sub(r"(?i)</(p|div|h[1-6]|li|blockquote)>", "\n\n", markup)
    markup = re.sub(r"(?i)<br\s*/?>", "\n", markup)
    text = html.unescape(re.sub(r"<[^>]+>", "", markup))
    text = "\n".join(line.rstrip() for line in text.splitlines())
    return re.sub(r"\n{3,}", "\n\n", text).strip()


def write(raw: pathlib.Path, date: str, title: str, origin: str, text: str) -> None:
    if len(text) < 400:
        print(f"  ~ skipped (too short to be a piece): {title}")
        return
    out = raw / f"{date}-{slug(title)}.md"
    out.write_text(
        f"# {title}\n\nsource: {origin}\ndate: {date}\n\n---\n\n{text}\n",
        encoding="utf-8",
    )
    print(f"  → sources/raw/{out.name}")


def parse_date(value: str) -> str:
    value = (value or "").strip()
    for fmt in ("%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S %z", "%Y-%m-%dT%H:%M:%S%z"):
        try:
            return datetime.datetime.strptime(value, fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    match = re.search(r"\d{4}-\d{2}-\d{2}", value)
    return match.group(0) if match else datetime.date.today().isoformat()


def ingest_feed(raw: pathlib.Path, body: str, origin: str) -> bool:
    try:
        root = ET.fromstring(body)
    except ET.ParseError:
        return False

    items = root.findall(".//item") or root.findall(f".//{ATOM}entry")
    if not items:
        return False

    for item in items:
        def text_of(*tags: str) -> str:
            for tag in tags:
                el = item.find(tag, CONTENT_NS) if ":" in tag else item.find(tag)
                if el is not None and (el.text or "").strip():
                    return el.text
            return ""

        title = html.unescape(text_of("title", f"{ATOM}title")).strip() or "untitled"
        date = parse_date(text_of("pubDate", f"{ATOM}published", f"{ATOM}updated"))
        markup = text_of("content:encoded", "description", f"{ATOM}content", f"{ATOM}summary")
        write(raw, date, title, origin, strip_html(markup))
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", required=True, type=pathlib.Path)
    ap.add_argument("--url")
    ap.add_argument("--file", type=pathlib.Path)
    args = ap.parse_args()
    args.raw.mkdir(parents=True, exist_ok=True)

    if args.file:
        text = args.file.read_text(encoding="utf-8", errors="replace")
        stamp = datetime.date.fromtimestamp(args.file.stat().st_mtime).isoformat()
        write(args.raw, stamp, args.file.stem, str(args.file), text.strip())
        return 0

    body = sys.stdin.read()
    if ingest_feed(args.raw, body, args.url or "feed"):
        return 0

    text = strip_html(body)
    heading = next((ln.strip() for ln in text.splitlines() if len(ln.strip()) > 12), "untitled")
    write(args.raw, datetime.date.today().isoformat(), heading[:60], args.url or "url", text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
