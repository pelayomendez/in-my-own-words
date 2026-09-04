#!/usr/bin/env bash
set -euo pipefail

# Fetches writing into sources/raw/ so the skill can distil traits from it.
#
#   ./add-source.sh https://example.com/feed       # RSS or Atom: every item
#   ./add-source.sh https://example.com/a-post     # one page
#   ./add-source.sh ~/drafts/piece.md              # a local file
#
# Ingest only. Trait extraction happens in conversation with the skill, because
# deciding whether a difference is a new habit or a one-off outlier needs a
# human. When this finishes, tell the skill:
#
#   "read the new sources in sources/raw and propose a profile update"

SKILL_DIR="$(cd "$(dirname "$0")/.." && pwd)"
RAW="$SKILL_DIR/sources/raw"
mkdir -p "$RAW"

if [[ $# -lt 1 ]]; then
  sed -n '4,14p' "$0" | sed 's/^#\{1,\} \{0,1\}//'
  exit 1
fi

for src in "$@"; do
  if [[ -f "$src" ]]; then
    echo "file: $src"
    python3 "$SKILL_DIR/scripts/_ingest.py" --raw "$RAW" --file "$src"
    continue
  fi

  echo "fetch: $src"
  if ! body="$(curl -fsSL --max-time 30 "$src")"; then
    echo "  ! could not fetch"
    continue
  fi
  printf '%s' "$body" | python3 "$SKILL_DIR/scripts/_ingest.py" --raw "$RAW" --url "$src"
done

echo
echo 'Next: "read the new sources in sources/raw and propose a profile update".'
