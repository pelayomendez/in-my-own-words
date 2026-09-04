---
name: sounds-like-me
description: "Draft, rewrite or audit long-form prose so it sounds like the configured author, in any language, using a voice profile distilled from their own published work. Use when the user asks to write an essay, newsletter, Substack post, blog article, talk script or long-form LinkedIn piece; asks to make a draft sound like them; asks whether a text sounds like them or where it goes off-voice; or asks to update their voice profile from new writing samples. Not for chat replies, commit messages or short operational email."
---

# sounds-like-me

A voice is not a tone setting. It is a set of decisions the author makes over and over — how long a paragraph runs before it breaks, when a metaphor is allowed in, which word gets the italics, how the last line lands. This skill holds those decisions in a profile and applies them.

Long-form only. Short-message register belongs to whatever always-on writing guidance the user already has; this skill takes over when structure and argument arc matter as much as word choice, and it should say so rather than fight for the same ground.

## Before anything

1. Read `config.yaml` in this skill directory. It names the author, the publication, the languages and where the profile lives. If it is still the unedited template, run **Bootstrap** below instead of guessing.
2. Work out the target language. For drafting and rewriting it is the language of the piece the user wants, taken from their request, not from the profile's primary language. For auditing there are two: the lexicon is chosen by the language of the **text under audit**, while the audit itself is written in the language the user is speaking to you in.
3. Load `references/core-voice.md` (language-agnostic) **and** the lexicon for the target language. Both, always. The core carries the structure; the lexicon carries the surface.
4. If the lexicon for that language is still a stub, say so in one line before delivering, and apply the core alone. Do not fake surface habits that have never been observed in that language.

## Mode 1 — Draft

The user gives ideas, notes, an outline, a voice memo, a mess. You return a finished piece.

- **Their argument order is the spec.** If the user has laid out ideas in a sequence, that sequence ships. Reordering it into a more conventional shape is the single most common way this goes wrong. When a reorder would genuinely help, deliver the piece in their order first, then say what you would move and why, in one sentence.
- **The ending is the payload.** Find the line that makes the whole piece land, and build backwards to it. If the user has told you what the ending is, nothing goes after it.
- Never invent a fact, a statistic, a source, an anecdote or a quotation. If the shape of the piece needs one, leave `[dato: …]` and name it in the handoff.
- One governing metaphor per piece, sustained end to end. Two metaphors is the tell of a machine reaching for whatever is nearest.
- Hit the word range in `config.yaml`. Long-form voices are calibrated at a length; the rhythm falls apart outside it.
- Offer a title and subtitle only if the profile records a title pattern.

## Mode 2 — Rewrite

The user hands you a draft — theirs, a colleague's, or something an AI produced — and wants it in their voice.

- Change the prose, not the argument. Same claims, same order, same evidence.
- Preserve anything already in voice. A rewrite that touches every sentence is a rewrite that ignored the draft.
- Watch for the specific failure of AI-generated Spanish and English drafts: staccato one-line paragraphs stacked into pseudo-verse. Most authors do not write that way; they write short paragraphs with occasional isolated lines used as punctuation. Check the profile's paragraph-length distribution and match it.
- Deliver the piece, then three to five bullets naming what you changed and why — tied to named profile traits, not to taste.

## Mode 3 — Audit

The user wants to know where a text stops sounding like them. Do not rewrite it.

Work through `references/audit-rubric.md`, judging against `references/core-voice.md` and the lexicon for the text's language — all three are already loaded from the steps above. Return a verdict per dimension with quoted evidence: the offending sentence, the trait it violates, and a one-line suggestion. End with the two or three fixes that would move the piece most. Quote, always — an audit without quotations is an opinion.

Separate what you can judge from what you can only flag. Voice is judgeable from the text. Whether a fact, quotation or anecdote is real is not — mark those **unverified** and list them for the author rather than passing or failing them.

## Mode 4 — Refresh the profile

Triggered by "learn from this", "add this to my profile", "this one is very me", or a new file appearing in `sources/`.

Follow `references/distilling.md`. In short: ingest the source, extract only traits that are **new or that contradict** what the profile already records, show the user the proposed diff before writing it, then update the profile files and append a row to `sources/index.md`. Never rewrite a profile file wholesale from a single new source — profiles accumulate, they do not get replaced.

Traits go to the layer they belong to. Argument moves, paragraph rhythm, how sections open and close, what earns a metaphor → `core-voice.md`. Specific words, punctuation habits, register, idiom, the tics → the lexicon for that source's language.

## Bootstrap (fresh fork)

`config.yaml` still says `YOUR NAME`, or the profile files are still stubs. Do not ask the user to describe their own style — people describe the writer they want to be. Ask instead for three to five published pieces, an RSS feed, or a folder of drafts, then run `references/distilling.md` from scratch to generate `core-voice.md` and the first lexicon. Fill `config.yaml` from what you learn and from a short conversation about scope and language. Show the profile before saving it.

Below three sources, say so: that is one article documented, not a voice. Offer to proceed anyway with the caveat recorded in `sources/index.md`.

`examples/ogilvy/` at the repo root is a complete worked profile. Read it before writing the first one — it is the fastest way to calibrate how specific these files have to get.

## Rules that hold in every mode

- The profile describes what the author *does*, not what good writing is. When the two disagree, the profile wins. Imperfections that are consistently theirs are part of the voice; do not sand them off.
- Never claim the author has read, done, met or felt something the sources do not support.
- Say when you are guessing. A one-line flag at the end beats a confident fabrication in the middle.
- The user is the last check. Deliver the piece, not a lecture about the piece.
