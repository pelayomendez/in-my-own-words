# sounds-like-me

**An agent skill that writes long-form in your voice — because it learned it from your own published work, not from a description of it.**

[pelayomendez.github.io/sounds-like-me](https://pelayomendez.github.io/sounds-like-me) · MIT

```bash
npx skills@latest add pelayomendez/sounds-like-me -g
```

Then: *bootstrap my voice profile from https://your-blog.com/feed*

---

## What it does

- **Draft** — you give it ideas, notes or a mess; it returns a finished piece.
- **Rewrite** — you give it a draft (yours, a colleague's, or something a model produced) and it puts it in your voice without touching your argument.
- **Audit** — you give it a text and it tells you, with quotations, where it stops sounding like you. It doesn't rewrite.
- **Refresh** — it reads new writing you point it at and updates the profile, so the voice tracks yours instead of freezing on the day you set it up.

## Why not just a style prompt

A style prompt is a description of how you'd like to sound. Ask anyone to describe their own writing and you get the writer they aspire to be: "clear, conversational, a bit witty". Every writer says this. It steers nothing.

This works the other way round. It reads what you've actually published and records what you demonstrably do — the paragraph-length distribution, how sentences start, which word gets the italics, what your last line does, and the phrases that never appear anywhere in your corpus. Every trait carries a verbatim quotation, so you can argue with it.

The anti-tells turn out to matter as much as the traits. Knowing that an author has never once written "it's important to note" does more to keep output in voice than any positive instruction.

## See a real one first

[`examples/ogilvy/`](./examples/ogilvy) is a complete worked profile for David Ogilvy. The mechanics of this tool are easy; the thing that's hard to picture is *how specific a profile has to get* before it does any work. That folder is the answer.

## Bilingual by construction

The profile is split in two layers:

- [`core-voice.md`](./skills/sounds-like-me/references/core-voice.md) — everything that survives translation. Shape, rhythm, argument moves, metaphor discipline, how a piece opens and lands. Almost none of it is about vocabulary.
- `lexicon.<lang>.md` — everything that doesn't. Words, punctuation habits, register, idiom, anti-tells.

Ask for a piece in a language whose lexicon is still a stub and it applies the core, derives only what safely follows, and tells you it's doing that. It will not invent verbal tics in a language it has never seen you write.

## Install

```bash
npx skills@latest add pelayomendez/sounds-like-me -g
```

`-g` installs globally, into `~/.claude/skills/`. Works with Claude Code, Codex, Cursor, OpenCode and ~70 other agents.

Or as a Claude Code plugin:

```
/plugin marketplace add pelayomendez/sounds-like-me
/plugin install sounds-like-me@pelayomendez
```

skills.sh copies the skill so you can edit it in place — which is what you want here, since the profile is meant to grow. The plugin keeps it as a read-only bundle you subscribe to.

## Set up your profile

Point it at your writing and say so. Three to five pieces is the floor; below that you're documenting one article, not a voice.

```
bootstrap my voice profile from https://your-blog.com/feed
```

It reads them, extracts the traits with evidence, shows you the profile, and only writes it once you've accepted. Then:

```
write this up for my newsletter: [your notes]
make this draft sound like me
does this sound like me?
```

## Keeping it current

Drop writing into `sources/raw/` and ask the skill to read it. Or batch it:

```bash
./skills/sounds-like-me/scripts/add-source.sh https://your-blog.com/feed
```

That only fetches text. The extraction happens in conversation, deliberately: deciding whether a difference is a new habit, a genre shift or a one-off is a judgement call, and a script that made it silently would rot the profile. Every accepted change appends a row to `sources/index.md`.

Profiles accumulate. A new source adds, sharpens or contradicts — it never triggers a rewrite. When a source contradicts the profile, the skill asks whether your voice is evolving, whether the genre differs, or whether that piece is an outlier, rather than averaging the two into mush.

## Privacy

Your profile and your corpus are yours. They live in the installed copy on your machine and nothing is uploaded anywhere. If you fork this to version your own profile, make the fork private — a voice profile is a fairly complete recipe for impersonating you.

## Working on this repo

```bash
npm run check
```

Catches what fails silently at runtime: unquoted YAML descriptions, a skill name drifting from its directory, a missing `agents/openai.yaml`, invocation mode out of sync between Claude Code and Codex, a skill absent from `plugin.json`, and a config pointing at profile files that don't exist.

Conventions follow [pelayomendez/pelayo-skills](https://github.com/pelayomendez/pelayo-skills), which follows [mattpocock/skills](https://github.com/mattpocock/skills).

Contributions welcome — especially lexicons for languages that don't have one yet, and audit-rubric dimensions that catch failures the current fifteen miss. See [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

MIT.
