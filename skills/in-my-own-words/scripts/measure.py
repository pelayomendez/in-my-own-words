#!/usr/bin/env python3
"""Measure a text against the author's measured baseline. No model involved.

    measure.py draft.md                    compare a draft to the baseline
    measure.py --baseline sources/raw/*.md  build the baseline from a corpus

Half of what makes prose sound like someone is countable: how long the
paragraphs run, how often a sentence opens on a conjunction, how many
one-line paragraphs there are. An audit that judges those by eye gets them
wrong in both directions — it flags a text that is fine and passes one that
is a model's rhythm wearing the author's words.

Reads and writes references/metrics.json. Standard library only.
"""

import argparse
import json
import pathlib
import re
import statistics
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
METRICS = HERE / "references" / "metrics.json"

DEFAULTS = {
    "language": "en",
    "openers": ["And", "But", "Because"],
    "burst": {"max_sentence_words": 6, "min_run": 3},
    "forbidden": [],
    "tolerance": 0.35,
}


# ---------------------------------------------------------------- parsing

def prose(text: str) -> str:
    """Strip everything that isn't the author's running prose."""
    text = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)      # frontmatter
    text = re.sub(r"```.*?```", "", text, flags=re.S)             # code fences
    keep = []
    for line in text.split("\n"):
        s = line.strip()
        if s.startswith("#") or s.startswith(">"):                # headings, quotes
            continue
        if re.match(r"^\s*([-*+]|\d+\.)\s", line):                # list items
            continue
        if re.match(r"^\s*\|", line):                             # tables
            continue
        keep.append(line)
    return "\n".join(keep)


def paragraphs(text: str):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def sentences(text: str):
    text = re.sub(r"\s+", " ", text)
    parts = re.split(r"(?<=[.!?…])\s+(?=[¿¡\"'«(\[]?[A-ZÁÉÍÓÚÑÜ])", text)
    return [p.strip() for p in parts if p.strip()]


def words(text: str) -> int:
    return len(re.findall(r"\b[\wÁÉÍÓÚÑÜáéíóúñü'’-]+\b", text))


# ---------------------------------------------------------------- measuring

def measure(text: str, cfg: dict) -> dict:
    body = prose(text)
    paras = paragraphs(body)
    sents = sentences(body)
    if not paras or not sents:
        sys.exit("nothing to measure")

    pw = [words(p) for p in paras]
    sw = [words(s) for s in sents]

    one_liner = sum(1 for p in paras if len(sentences(p)) == 1)
    openers = tuple(cfg["openers"])
    opened = [s for s in sents if s.split() and s.split()[0].strip(",;:").capitalize()
              in [o.capitalize() for o in openers]]

    b = cfg["burst"]
    runs, run = 0, 0
    for n in sw:
        run = run + 1 if n <= b["max_sentence_words"] else 0
        if run == b["min_run"]:
            runs += 1
    total = sum(sw)

    hits = []
    low = body.lower()
    for phrase in cfg.get("forbidden", []):
        n = low.count(phrase.lower())
        if n:
            hits.append((phrase, n))

    return {
        "words": total,
        "paragraphs": len(paras),
        "paragraph_words_median": round(statistics.median(pw), 1),
        "paragraph_words_range": [min(pw), max(pw)],
        "single_sentence_paragraph_pct": round(100 * one_liner / len(paras), 1),
        "sentences": len(sents),
        "sentence_words_median": round(statistics.median(sw), 1),
        "short_sentence_pct": round(100 * sum(1 for n in sw if n <= 5) / len(sw), 1),
        "long_sentence_pct": round(100 * sum(1 for n in sw if n >= 25) / len(sw), 1),
        "opener_pct": round(100 * len(opened) / len(sents), 1),
        "bursts_per_1000w": round(1000 * runs / total, 1) if total else 0,
        "_openers": [s[:58] for s in opened],
        "_forbidden": hits,
    }


# ---------------------------------------------------------------- reporting

COMPARED = [
    ("words", "words", None),
    ("paragraph_words_median", "median words per paragraph", "paragraph_words_median"),
    ("single_sentence_paragraph_pct", "one-sentence paragraphs %", "single_sentence_paragraph_pct"),
    ("sentence_words_median", "median words per sentence", "sentence_words_median"),
    ("short_sentence_pct", "sentences of 5 words or fewer %", "short_sentence_pct"),
    ("opener_pct", "sentences opening on a conjunction %", "opener_pct"),
    ("bursts_per_1000w", "short-sentence bursts per 1000 words", "bursts_per_1000w"),
]


def report(m: dict, cfg: dict) -> int:
    targets = cfg.get("targets", {})
    tol = cfg.get("tolerance", 0.35)
    off = 0

    print(f"\n  {'':44}{'this text':>11}{'baseline':>11}")
    print("  " + "─" * 66)

    rng = targets.get("words")
    for key, label, tkey in COMPARED:
        got = m[key]
        if key == "words" and rng:
            want, bad = f"{rng[0]}–{rng[1]}", not (rng[0] <= got <= rng[1])
        elif tkey and tkey in targets:
            t = targets[tkey]
            want = str(t)
            bad = abs(got - t) > max(tol * t, 0.6)
        else:
            want, bad = "—", False
        off += bad
        print(f"  {label:44}{got:>11}{want:>11}  {'←' if bad else ''}")

    if m["_forbidden"]:
        print(f"\n  Phrases the profile forbids ({len(m['_forbidden'])}):")
        for phrase, n in m["_forbidden"]:
            print(f"    ×{n}  {phrase}")
        off += 1

    if m["_openers"]:
        print(f"\n  Conjunction openings ({len(m['_openers'])}):")
        for s in m["_openers"][:12]:
            print(f"    · {s}")

    print()
    if not off:
        print("  Within range on every measure. Voice is still a judgement call —")
        print("  run the audit for the parts that aren't countable.\n")
    else:
        print(f"  {off} measure(s) outside the baseline. These are numbers, not verdicts:")
        print("  a deviation is a question to answer, not automatically a defect.\n")
    return 1 if off else 0


def build(paths, cfg) -> dict:
    texts, n = [], 0
    for p in paths:
        f = pathlib.Path(p)
        if f.is_file():
            texts.append(f.read_text(encoding="utf-8", errors="replace"))
            n += 1
    if not texts:
        sys.exit("no readable sources")
    m = measure("\n\n".join(texts), cfg)
    print(f"  Baseline from {n} source(s), {m['words']} words.\n")
    return {
        "language": cfg["language"],
        "openers": cfg["openers"],
        "burst": cfg["burst"],
        "forbidden": cfg.get("forbidden", []),
        "tolerance": cfg.get("tolerance", 0.35),
        "corpus": {"sources": n, "words": m["words"]},
        "targets": {k: m[k] for k in (
            "paragraph_words_median", "single_sentence_paragraph_pct",
            "sentence_words_median", "short_sentence_pct",
            "long_sentence_pct", "opener_pct", "bursts_per_1000w")},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--baseline", action="store_true",
                    help="build references/metrics.json from these files instead of comparing")
    a = ap.parse_args()

    cfg = dict(DEFAULTS)
    if METRICS.exists():
        cfg.update(json.loads(METRICS.read_text()))

    if a.baseline:
        out = build(a.files, cfg)
        METRICS.parent.mkdir(parents=True, exist_ok=True)
        METRICS.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
        print(json.dumps(out["targets"], indent=2, ensure_ascii=False))
        print(f"\n  Written to {METRICS.relative_to(HERE)}")
        print("  Build it only from sources whose provenance is `hand`.\n")
        return 0

    if "targets" not in cfg:
        sys.exit("No baseline yet. Run with --baseline over your hand-written corpus first.")
    text = "\n\n".join(pathlib.Path(f).read_text(encoding="utf-8", errors="replace")
                       for f in a.files)
    return report(measure(text, cfg), cfg)


if __name__ == "__main__":
    raise SystemExit(main())
