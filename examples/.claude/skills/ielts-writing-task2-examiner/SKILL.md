---
name: ielts-writing-task2-examiner
description: >
  IELTS Writing Task 2 examiner — evaluates, corrects, and rephrases Academic or General Training Task 2 essays.
  Use when the user pastes an IELTS Writing Task 2 question and their essay and wants:
  (1) band scores on each official criterion (TR, CC, LR, GRA) plus an overall band score,
  (2) inline Markdown corrections on the original essay (strikethrough errors, inline code for corrections),
  (3) detailed correction analysis, and
  (4) a Band 7–9 model paraphrase with analysis.
  Triggers on phrases like "批改 Task 2", "evaluate my IELTS writing", "IELTS Task 2 correction",
  or any submission of an IELTS Task 2 prompt + essay.
---

# IELTS Writing Task 2 — Examiner Skill

## References

Read these files before evaluating:

- **[assessment-criteria.md](references/assessment-criteria.md)** — official IELTS Task 2 criteria definitions for TR, CC, LR, GRA
- **[band-descriptors-task2.md](references/band-descriptors-task2.md)** — official band descriptors table (Band 0–9) for Task 2

## Workflow

Execute all five sections in order and write them to a Markdown file.

### Output File

Create a file in the **current working directory** (where the user ran Claude Code, i.e., `$PWD`) named:

```
IELTS-Writing-Task2-YYYYMMDD.md
```

Use today's date. Write all sections below into this file.

---

### Section 1 — Band Scores

Score each criterion independently using the band descriptors. Scores are in whole or half bands (e.g. 6.0, 6.5, 7.0).

```
## Band Scores

| Criterion                    | Band |
|------------------------------|------|
| Task Response (TR)           | X.X  |
| Coherence & Cohesion (CC)    | X.X  |
| Lexical Resource (LR)        | X.X  |
| Grammatical Range & Accuracy | X.X  |
| **Overall**                  | **X.X** |
```

Overall = average of the four criteria, rounded to nearest 0.5.

For each criterion, write 1–2 sentences justifying the score.

---

### Section 2 — Corrected Essay

Reproduce the user's **original essay verbatim**, applying inline Markdown corrections only:

- `~~wrong phrase~~` `correct phrase` — for errors that need replacement (strikethrough the wrong, inline code the correct)
- `` `inserted word` `` — for missing words that need to be inserted (no strikethrough needed)
- Leave correct text untouched

**Correction format example:**

> I think skill stacking is a necessary ability for people in this generation. Because of `the` fast development of technology, some skills people learned ~~in least year~~ `last year` ~~maybe have been outdated today~~ `may already be outdated today`.

Do **not** rewrite the essay. Only mark errors inline using the above Markdown syntax.

---

### Section 3 — Correction Analysis

Provide a detailed breakdown organised by criterion:

- **Task Response**: Position clarity, idea development, relevance, support — what was argued well / what was missing, underdeveloped, or off-topic
- **Coherence & Cohesion**: Paragraphing, logical flow, cohesive device usage
- **Lexical Resource**: Vocabulary range, word choice errors, collocations, spelling
- **Grammatical Range & Accuracy**: Grammar errors listed with explanations, sentence structure variety

For each error identified in the corrected essay, explain *why* it is wrong and *what the correct form should be*.

---

### Section 4 — Band 7–9 Model Answer

Write a model answer that:

- **Follows the same general direction and main ideas** as the user's essay (same stance, same key arguments — not a completely different position)
- Targets **Band 7–9**: clear, accurate, varied — not overly sophisticated or unlearnable
- Uses natural academic/formal register appropriate to Task 2
- Is appropriately structured: introduction with a clear thesis, body paragraphs each with one main idea, and a conclusion
- Meets the 250-word minimum
- **Bolds every high-band vocabulary phrase and grammar structure** that will be highlighted in Section 5 — this lets the reader spot learning points at a glance without cross-referencing the analysis tables

Label this section:

```
## Band 7–9 Model Answer
```

**Bolding convention:** Bold the exact word or phrase as it appears in the model answer. If a grammar structure spans a full sentence (e.g., a mid-sentence adverbial), bold the whole sentence. Ensure every item that appears in the Section 5 vocabulary table or grammar table is bolded in the model answer.

---

### Section 5 — Model Answer Analysis

Analyse the model answer to help the user learn from it. Use exactly these four subsections in this order:

#### `### High-Band Vocabulary`
A table with three columns: **Model answer phrase | User's version | Why it is stronger**
- "User's version" is the phrase the user actually wrote (or "(not present)" if the user omitted the point entirely)
- "Why it is stronger" explains the register, precision, or collocation advantage

#### `### Structural Choices`
Table or numbered list explaining: how the thesis is constructed (concessive + main claim), how body paragraphs develop each idea (claim → mechanism → consequence), how the pivot between arguments is signalled, and how the conclusion synthesises rather than restates.

#### `### Grammar Structures That Elevate the Response`
A table with three columns: **Structure | Example from model | Effect**
- Bold every entry in the **Structure** column
- "Example from model" quotes the exact phrase from the model answer

#### `### Key Differences from Your Essay`
A table with three columns: **Your essay | Model answer | Why the model is stronger**
- Compare the most impactful differences — word choice, structural moves, underdeveloped arguments, register issues
- Tie each row back to a specific criterion (TR, CC, LR, or GRA) where helpful

Label this section:

```
## Model Answer Analysis
```

---

## Notes

- Maintain the perspective of a **professional senior IELTS examiner** throughout — objective, evidence-based, constructive
- Do not over-correct: only mark genuine errors, not stylistic preferences
- Task 2 requires a clear, developed **position** — check whether the user's thesis is stated upfront and whether each body paragraph has a clear topic sentence that supports it
- Over-generalisation (asserting claims without support) is explicitly penalised at Band 7 — flag it when present
- Paragraphing is critical for Task 2 CC: absence of paragraphing or unclear paragraph topics must be called out
- Word count below 250 words must be flagged and will negatively affect all criteria scores
