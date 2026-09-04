# Sources

The evidence base. Every trait in `../references/` should trace back to something in here.

## Adding a source

Drop it in `raw/` and tell the skill:

> Añade esto a mi perfil de voz
> Learn from this piece
> This one is very me — pick up what's different about it

The skill reads it, extracts only what is **new or contradictory**, shows you the proposed change, and appends a row to `index.md` once you accept. It never rewrites a profile file from a single source.

`scripts/add-source.sh` is the batch path: it fetches an RSS feed or a URL into `raw/` with a dated slug. It only ingests text — the trait extraction is the skill's job, in conversation, because the interesting decisions (is this a new habit or an outlier?) need a human.

## Naming

`raw/YYYY-MM-DD-slug.md`, one file per piece, verbatim. Keep the original text unedited: it is the evidence for every future refresh, including ones that revisit an earlier judgement.

Mark a piece you are unhappy with in its `index.md` row rather than leaving it out. Knowing which of your own writing you consider off-voice is useful signal.
