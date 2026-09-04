# Contributing

## Changing the mechanism

`SKILL.md`, `references/distilling.md`, `references/audit-rubric.md`, `scripts/`.

Keep it author-agnostic — a fork should need to touch nothing but `config.yaml`, `references/core-voice.md`, the lexicons and `sources/`. If you find yourself writing "Pelayo" or "Substack" into the mechanism, it belongs in the profile instead.

Prose, not code. Short and imperative.

## Changing the profile

Only through Mode 4. Ingest a real source, extract the traits, show the diff, then write. Every trait carries a verbatim quotation.

Route each trait to the right layer:

| Trait | Layer |
|---|---|
| Structure, paragraph rhythm, argument moves, metaphor policy, opening and closing patterns, evidence habits, stance | `core-voice.md` |
| Words, connectors, punctuation, register, idiom, formatting, anti-tells | `lexicon.<lang>.md` |

Then append a row to `sources/index.md`. A trait with no source row behind it will be treated as noise by the next audit of the profile.

## Adding a language

1. Add it to `languages.also` in `config.yaml`.
2. Create `references/lexicon.<lang>.md` from `lexicon.en.md`'s stub shape — keep the **Status: stub** line until real sources exist.
3. Ingest at least three pieces the author wrote *natively* in that language. Translations of their own work don't count; they carry the source language's syntax.
4. `npm run check` fails if a declared language has no lexicon, or a lexicon exists for an undeclared language.

## Rules that bite

- **Quote the `description`** in `SKILL.md` frontmatter. An unquoted value containing `: ` is invalid YAML; Claude Code tolerates it, `npx skills` silently skips the skill.
- **Keep both harnesses in sync.** `disable-model-invocation: true` and `policy.allow_implicit_invocation: false` travel together. This skill is model-invocable, so neither is set.
- **Bump `version` in `.claude-plugin/plugin.json`** when you change what plugin subscribers receive. Profile updates count.
- **`sources/raw/` is verbatim.** Never clean up an ingested source. It's the evidence for every future refresh, including ones that revisit an earlier call.
- Run `npm run check` before committing.
