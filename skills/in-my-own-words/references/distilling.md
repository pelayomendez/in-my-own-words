# Distilling and refreshing a voice profile

How a profile gets built from real writing, and how it grows without drifting.

## Principles

- **Observe, don't prescribe.** Record what the author does, including the parts a style guide would flag. Consistent imperfection is signal.
- **Quote or it didn't happen.** Every trait carries at least one verbatim example. A trait without evidence is your taste leaking into their profile.
- **Two layers, always.** Anything that survives translation goes to `core-voice.md`. Anything that dies in translation goes to a lexicon.
- **Accumulate, never replace.** A new source adds, sharpens or contradicts. It does not trigger a rewrite of the profile.
- **Show the diff first.** Never silently edit a profile file. Propose, let the author accept, then write.

## Ingesting a source

Accepted: a URL, an RSS feed, a pasted text, a file dropped into `sources/`, a folder of drafts.

1. Get the full text. For a Substack or blog, the RSS feed carries whole posts and is more reliable than scraping a client-rendered page. Truncated feed items need a direct fetch of the post.
2. Save it under `sources/raw/` with a dated slug: `2026-07-05-codigos-secretos.md`. Keep it verbatim — the raw text is the evidence base for every future refresh.
3. Note the language and whether the author considers it representative. A piece they dislike is still useful, but it should be marked as such rather than weighted the same.

## Extracting traits

Work through these dimensions and write down what you actually observe, with quotations:

1. **Length and shape.** Word count. How many movements. Where the thesis lands.
2. **Openings and closings.** Quote the first and last lines verbatim. These are the highest-signal sentences in any corpus.
3. **Paragraph rhythm.** Measure it. What proportion of paragraphs are one line? What is the typical sentence count? Do short lines cluster, and where?
4. **Headings.** Grammatical form, not just topic. Noun phrase, declarative, imperative, question?
5. **Sentence-level fingerprints.** How sentences start. Fragments. Conjunction openings. Repeated syntactic frames.
6. **Argument moves.** The recurring rhetorical shapes — the reframe, the concession, the reversal. This is the deepest layer and the one most worth getting right.
7. **Metaphor policy.** How many per piece, sustained or scattered, drawn from which domains.
8. **Evidence habits.** Named sources or vague attribution? Concrete numbers or round ones? Links?
9. **Lexicon.** Connectors, filler, favourite nouns, adjective patterns, register, colloquialisms, foreign words, how jargon is treated.
10. **Punctuation and formatting.** Dashes, quotation systems, italics, bold, code formatting, numerals, captions.
11. **Stance.** Person, address to the reader, hedging level, humour, humility.
12. **Level of polish.** Do typos survive? Is the copy clean?
13. **Anti-tells.** What never appears. This list does as much work as the positive traits.

## Writing the update

For each trait, decide:

- **New** → add it to the right layer, with its quotation.
- **Confirms** → add the new quotation only if it is a better example than what is there. Do not pile up evidence for settled traits.
- **Contradicts** → this is the interesting case. Do not average the two. Ask whether the voice is evolving (newer source wins, note the shift and the date), whether the genre differs (record both, scoped by genre), or whether one piece is an outlier (leave the profile alone, note the exception).

Then append a row to `sources/index.md`: date, title, language, link, and what the profile learned from it. That row is how a future session knows what has already been read.

## Bootstrapping from nothing

Same procedure, but ordered for efficiency: read every source before writing anything, since traits only become visible as repetition. Three sources is the minimum for a usable profile; five is comfortable. Below three you are describing one article, not a voice.

Do not interview the author about their own style as the primary method. People describe the writer they aspire to be. Use the interview only for scope decisions — which genres this covers, which languages, target length, whether to offer titles — and take the style itself from the text.

## Keeping it honest

Re-read the whole profile once every ten or so ingested sources. Profiles rot in two ways: traits that were true of early writing and no longer are, and traits that were always just one article. Both show up as rules that no recent source supports. Cut them.
