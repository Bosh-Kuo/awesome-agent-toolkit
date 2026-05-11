---
name: ielts-writing-task1-examiner
description: >
  IELTS Writing Task 1 examiner — evaluates, corrects, and rephrases Academic or General Training Task 1 essays.
  Use when the user pastes an IELTS Writing Task 1 question and their essay and wants:
  (1) band scores on each official criterion (TA, CC, LR, GRA) plus an overall band score,
  (2) inline Markdown corrections on the original essay (strikethrough errors, inline code for corrections),
  (3) detailed correction analysis, and
  (4) a Band 7–9 model paraphrase with analysis.
  Triggers on phrases like "批改 Task 1", "evaluate my IELTS writing", "IELTS Task 1 correction",
  or any submission of an IELTS Task 1 prompt + essay.
---

# IELTS Writing Task 1 — Examiner Skill

## References

Read these files before evaluating:

- **[assessment-criteria.md](references/assessment-criteria.md)** — official IELTS criteria definitions for TA, CC, LR, GRA
- **[band-descriptors-task1.md](references/band-descriptors-task1.md)** — official band descriptors table (Band 0–9) for Task 1

## Workflow

Execute all five sections in order and write them to a Markdown file.

### Output File

Create a file in the **current working directory** (where the user ran Claude Code, i.e., `$PWD`) named:

```
IELTS-Writing-Task1-YYYYMMDD.md
```

Use today's date. Write all sections below into this file.

---

### Section 1 — Band Scores

Score each criterion independently using the band descriptors. Scores are in whole or half bands (e.g. 6.0, 6.5, 7.0).

```
## Band Scores

| Criterion                    | Band |
|------------------------------|------|
| Task Achievement (TA)        | X.X  |
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

- **Task Achievement**: What was covered well / what was missing or inaccurate
- **Coherence & Cohesion**: Paragraphing, logical flow, cohesive device usage
- **Lexical Resource**: Vocabulary range, word choice errors, collocations, spelling
- **Grammatical Range & Accuracy**: Grammar errors listed with explanations, sentence structure variety

For each error identified in the corrected essay, explain *why* it is wrong and *what the correct form should be*.

---

### Section 4 — Band 7–9 Model Answer

Write a model answer that:

- **Follows the same general direction and main ideas** as the user's essay (same key points, same data interpretation, same letter purpose — not a completely different angle)
- Targets **Band 7–9**: clear, accurate, varied — not overly sophisticated or unlearnable
- Uses natural academic/formal register appropriate to Task 1
- Is appropriately structured with an overview/introduction, body paragraphs, and (for Academic) a clear overview of key trends
- Meets the 150-word minimum
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
Numbered list explaining how the model is organised — overview placement, data grouping strategy, paragraph sequencing, and how the model's structure improves on the user's.

#### `### Grammar Structures That Elevate the Response`
A table with three columns: **Structure | Example from model | Effect**
- Bold every entry in the **Structure** column
- "Example from model" quotes the exact phrase from the model answer

#### `### Key Differences from Your Essay`
A table with three columns: **Your essay | Model answer | Why the model is stronger**
- Compare the most impactful differences — word choice, structural moves, missing data points
- Tie each row back to a specific criterion (TA, CC, LR, or GRA) where helpful

Label this section:

```
## Model Answer Analysis
```

---

## Notes

- Maintain the perspective of a **professional senior IELTS examiner** throughout — objective, evidence-based, constructive
- Do not over-correct: only mark genuine errors, not stylistic preferences
- For Academic Task 1: pay special attention to whether the overview is present and whether key trends are identified (not just mechanical data listing)
- For General Training Task 1: pay special attention to tone, register, and whether all three bullet points are fully addressed
- Word count below 150 words must be flagged and will negatively affect all criteria scores
