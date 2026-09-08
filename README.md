# in-my-own-words

**AI that writes like you, because it's read you.**

A skill you install into Claude Code, Cursor, Codex or any of the ~70 agents that support them. Give it a few things you've already written — posts, a newsletter, a talk, internal docs, whatever exists. It works out how you actually write, then writes new pieces in your voice, fixes drafts that came out sounding like a robot, and tells you when something doesn't sound like you.

[pelayomendez.github.io/in-my-own-words](https://pelayomendez.github.io/in-my-own-words) · MIT

```bash
npx skills@latest add pelayomendez/in-my-own-words -g
```

Then: *learn my writing voice from the files in ~/writing/*

---

## Five things it does

- **Write** — give it ideas, an outline or a mess of bullet points; it returns a finished piece. It keeps your ideas in the order you gave them.
- **Rewrite** — hand it a draft (yours, a colleague's, or something an AI produced). Same points, same order, same facts; it only changes how it's written, and tells you what it touched.
- **Check** — it quotes the exact sentences that stopped sounding like you, and says why. It won't rewrite them; that part stays yours.
- **Grill** — it interviews you, but never with "describe your style". It shows you two versions of your own sentence and asks which is more you, then reports where your answers and your writing disagree.
- **Keep up** — show it something new you've published and it picks up only what's changed, so the profile tracks you instead of freezing on the day you set it up.

## Why telling an AI to "write like me" never works

Ask any writer to describe their own style and you get the same three words: clear, conversational, a bit witty. It's what we'd all like to be true, and it tells an AI nothing.

So this goes the other way round. It reads what you've published and writes down what you actually do — how long your paragraphs run, how your sentences start, which word you put in italics, how you end a piece. Every single thing it notices comes with a quote from your own writing, so you can look at it and say: no, that's not me, that was one article.

The most useful part turned out to be the opposite list. Knowing that you have never once typed "it's important to note" keeps a draft sounding like you better than any instruction about what to write.

## The part nobody else does

The grill puts what you *say* about your writing next to what you *do*, and shows you the gap:

> You said you keep things short. Your last five pieces average 1,400 words.
>
> You said you always cut adverbs in the final pass. There are 31 in the corpus, nine of them in the piece you named as your best.

Your answers don't win those arguments — the corpus does. Stated preferences describe the writer you mean to be, and writing to intent instead of practice is the failure this whole thing exists to prevent. The one exception is audience and scope, which no amount of reading can tell you.

Writing by *other people* that you admire is deliberately never collected. It's the obvious next feature and it would quietly wreck the profile: feed it in and the output drifts toward that writer, and you won't be able to say why the drafts feel slightly off.

## It asks who actually wrote it

Every voice tool assumes your published work is yours. In 2026 that assumption is broken for most people who publish, and it fails quietly: distil a profile from model-assisted writing and it learns the model's habits, files them under your name, and hands you drafts that feel subtly wrong for reasons you can't put your finger on.

So each source carries a provenance — `hand`, `assisted`, `drafted` — and it changes what gets trusted. If you supplied the structure and a model supplied the sentences, the argument layer is still yours and the lexicon isn't; the profile is split along that exact line, so half of it survives.

There's a nice inversion in it. A phrase that appears only in your model-assisted pieces, and that you reject when the grill puts it in front of you, isn't a habit you're dropping — it's the model's, in your mouth. It doesn't get deleted. It goes into your anti-tells, so it can't come back.

## See a real one first

[`examples/ogilvy/`](./examples/ogilvy) is a complete worked profile for David Ogilvy. The mechanics of this tool are easy; the thing that's hard to picture is *how specific a profile has to get* before it does any work. That folder is the answer.

## Bilingual by construction

The profile is split in two layers:

- [`core-voice.md`](./skills/in-my-own-words/references/core-voice.md) — everything that survives translation. Shape, rhythm, argument moves, metaphor discipline, how a piece opens and lands. Almost none of it is about vocabulary.
- `lexicon.<lang>.md` — everything that doesn't. Words, punctuation habits, register, idiom, anti-tells.

Ask for a piece in a language whose lexicon is still a stub and it applies the core, derives only what safely follows, and tells you it's doing that. It will not invent verbal tics in a language it has never seen you write.

## Install

```bash
npx skills@latest add pelayomendez/in-my-own-words -g
```

`-g` installs globally, into `~/.claude/skills/`. Works with Claude Code, Codex, Cursor, OpenCode and ~70 other agents.

Or as a Claude Code plugin:

```
/plugin marketplace add pelayomendez/in-my-own-words
/plugin install in-my-own-words@pelayomendez
```

skills.sh copies the skill so you can edit it in place — which is what you want here, since the profile is meant to grow. The plugin keeps it as a read-only bundle you subscribe to.

## Set up your profile

A folder, a feed, or a few pieces pasted in. Published or not — a talk script and a long internal doc carry a voice as well as a blog post does. Three to five is the floor; below that you're documenting one piece, not a voice.

```
learn my writing voice from the files in ~/writing/
learn my writing voice from https://your-site.com/feed
```

It reads them, extracts the traits with evidence, shows you the profile, and only writes it once you've accepted. Then:

```
write this up for my newsletter: [your notes]
make this draft sound like me
does this sound like me?
```

## Keeping it current

Drop writing into `sources/raw/` and ask the skill to read it. Or batch it — the script takes a feed, a page or local files:

```bash
./skills/in-my-own-words/scripts/add-source.sh https://your-site.com/feed
./skills/in-my-own-words/scripts/add-source.sh ~/writing/talk-2026.md ~/writing/rfc.md
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
