# Audit rubric

For Mode 3. Judge a text against the profile, dimension by dimension. Do not rewrite.

Judge against `core-voice.md` plus the lexicon for the **language the text is written in**. Write the audit itself in the language the user is speaking to you in.

For each dimension return: **verdict** (on voice / drifting / off voice / unverifiable), **evidence** (a verbatim quotation from the text), **trait** (the named profile trait it meets or violates), **fix** (one line, not a rewrite).

Skip dimensions the text has no occasion to exercise. Report every dimension that genuinely fails, however many that is — but say plainly when a text is largely on voice instead of padding the list to look thorough. Both failure modes are real; neither is fixed by a quota.

Dimensions 4, 5, 7 and 13 are partly countable. Run `../scripts/measure.py <file>` and use its numbers rather than your impression of them; a deviation it reports is a question, not automatically a defect.

## Dimensions

1. **Length and register.** Inside the target range? Does the register match what the piece is doing — trade for a piece that hands the reader a practice, essay for one that argues a claim — and does it hold throughout? A piece in the wrong register for its purpose is a finding even when it holds that register consistently.
2. **Opening.** Scene, symptom or personal friction — or does it open by defining the topic? Opening on a definition is the most common failure and the most damaging.
3. **Structure.** Four movements present? Does a hinge sentence plant the thesis early, alone?
4. **Paragraph rhythm.** *(measured)* Count words per paragraph and compare the distribution to the register the piece should be in. Flag the two failure modes explicitly: a wall of one-line paragraphs stacked like verse, and uniform blocks with no short lines at all.
5. **The burst.** *(measured)* Does a run of three or four sentences under 12 words appear every few paragraphs? Its absence makes a text technically correct and tonally dead.
6. **Headings.** Right grammatical form? Any question-headings? Any numbering?
7. **Sentence openings.** *(measured)* Are there And / But / Because starts? Any deliberate fragments? Their total absence is a strong tell.
8. **Argument moves.** Is the reframe present — "what's expensive is no longer X, it's Y"? **Count the instances**: two or three is the voice, five is a template. Are concessions made with concrete examples rather than formulas?
9. **Metaphor.** Exactly one governing metaphor, sustained? Apply the recurrence test in `core-voice.md`: a source domain that returns after the section introducing it is governing, and a second governing metaphor is an automatic finding. Incidental one-off analogies are not.
10. **Evidence.** Named sources and specific numbers, or "experts agree" and round figures? Are there links?
11. **Verifiability.** *Separate from voice.* List every factual claim, statistic, quotation, book, name and anecdote in the text, and mark each one **verified** (you checked it), **unverifiable from the text alone**, or **wrong** (you know it to be false). Do not pass or fail the piece on these — hand the list to the author. A fabricated attribution does more damage than any stylistic miss, and the only reliable way to catch one is to enumerate them.
12. **Voice and stance.** Person and address: first person for opinion, the "we" of the trade, direct address to the reader. Is the reader addressed at all, especially in the final third? Hedging calibrated — firm on observation, tentative on projection? Any moralising, alarmism or promotional enthusiasm? Is there one dry line of humour? Check these against the stance section of `core-voice.md` and the address habits in the lexicon.
13. **Lexicon and anti-tells.** *(partly measured — the forbidden list is in `metrics.json`)* Scan for the forbidden list in the relevant lexicon, and for the positive habits it records — connectors, sentence openings, favourite constructions. Quote every hit in both directions.
14. **Formatting.** Dash usage, quotation systems, italics for single-word emphasis, bold used only to coin, no emoji, no tables in the prose.
15. **Closing.** Does it return to the opening image? Two short contrasting sentences? Is the last line the shortest? Does anything follow what should have been the ending? A piece that keeps going past its own best last line is the most expensive finding on this list.

## Output

A verdict list — or a table, which is fine here even where the lexicon forbids tables in prose, because an audit is a report and not a piece in the author's voice. Then a short section: **the two or three fixes that would move this most**, ranked by impact rather than by order of appearance. Keep the verifiability list separate from the voice findings so the author can act on it independently.
