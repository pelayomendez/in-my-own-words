# Working in this repo

One skill, `skills/in-my-own-words`, plus the profile it runs on.

Two kinds of file live here and they have opposite rules:

- **Mechanism** — `SKILL.md`, `references/distilling.md`, `references/audit-rubric.md`, the scripts. Generic, author-agnostic, forkable. No individual author belongs in these.
- **Profile** — `config.yaml`, `references/core-voice.md`, `references/lexicon.*.md`, `sources/`. Entirely author-specific, and only ever changed by distilling from a real source. In this repo they ship as **empty templates**; a real profile lives in the user's installed copy, never here.

`examples/ogilvy/` is the exception and the reference standard: a complete worked profile, kept current with the schema in `references/`. When you change what a profile section should contain, update the example in the same commit or it stops being the thing people calibrate against.

Never commit a real person's profile or corpus to this repo. A voice profile is a fairly complete recipe for impersonating someone.

Never hand-edit a profile file to make an output better. If a piece came out wrong, either the profile is missing a trait — in which case find the source that evidences it and run the refresh properly — or the profile is right and the output was a miss. Editing the profile to fix one output is how it stops describing anyone.

`references/core-voice.md` holds only what survives translation. If a trait dies in translation, it belongs in a lexicon. Getting this boundary wrong is what makes the English output read like translated Spanish.

Follow [`CONTRIBUTING.md`](./CONTRIBUTING.md) and run `npm run check` before committing.
