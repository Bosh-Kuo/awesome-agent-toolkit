---
name: product-prd
description: "Generate a high-level Product Requirements Document (PRD) for a new product or project at inception stage. Focuses on product vision, core objectives, user personas, key feature groups (not individual feature specs), architecture overview, and phased roadmap. Use when starting a new project, aligning stakeholders on the north star, or establishing overall product direction — NOT for speccing individual features (use SDD/spec-writer for that). Triggers on: create a PRD, write a product PRD, plan a new product, product requirements, high-level product spec, product vision document."
---

# Product PRD Generator

Generate a high-level Product Requirements Document that establishes product vision and direction — not feature specs. Individual feature specs belong in SDD / spec-writer tools.

**Output location:** Project root as `PRD.md`

---

## Resources

- **Template:** [templates/PRD.md](templates/PRD.md) — the PRD structure to fill in
- **Example:** [examples/PRD.md](examples/PRD.md) — a complete filled-in reference

Read `templates/PRD.md` before generating output to use the exact format.

---

## The Job

1. **Understand** what the user has already described
2. **Brainstorm** — identify gaps and align on vision through targeted questions
3. **Generate** the PRD using `templates/PRD.md` as the format
4. **Save** to `PRD.md` at the project root

---

## Step 1: Gap Analysis (not a fixed questionnaire)

The user will typically describe their product idea when invoking this skill. **Do not ask a preset list of questions.** Instead:

1. Read what the user has already shared
2. Map their description against the 10 PRD sections
3. Identify which dimensions are unclear or missing:
   - **Problem & audience** — who has this pain? how acute is it?
   - **Vision** — what transformative outcome does this enable?
   - **Scope** — what's in for MVP vs later?
   - **Success** — how will you know it worked?
   - **Constraints** — tech stack, timeline, team size, non-starters?
4. Ask only the 2–4 most critical questions that are genuinely unresolved — based on what the user said, not a template

**Key principle:** The user's initial description is a starting point for a conversation, not just input to a form. Engage, reflect back your understanding, and surface assumptions together before writing.

If the user's description is already detailed enough for a particular dimension, skip that question entirely.

---

## Step 2: Generate the PRD

Once you have enough context, generate the PRD following the structure in `templates/PRD.md`.

Guidelines:
- **Feature Groups (Section 5):** High-level capability groups only. No acceptance criteria, no implementation detail. If a bullet needs more than one sentence to explain, it belongs in a feature spec.
- **Objectives (Section 3):** Must be measurable. "Easy to use" or "Fast" are not objectives. "User completes core task in < 2 minutes" is.
- **Out of Scope (Section 7):** Be explicit. This section prevents scope creep more than any other.
- **Architecture (Section 6):** If tech stack is undecided, write `TBD` — do not guess or recommend.
- **Language:** Write the PRD in English to match the template.

---

## Step 3: Save

Save to `PRD.md` at the **project root** (not in `docs/` or any subdirectory).

---

## Quality Checklist

Before saving:

- [ ] Read `templates/PRD.md` and followed the exact format
- [ ] Asked targeted questions based on actual gaps — not a fixed list
- [ ] Vision statement is a single sentence
- [ ] All objectives are measurable
- [ ] Feature groups are high-level — no acceptance criteria
- [ ] Non-goals explicitly defined
- [ ] Roadmap shows at least MVP → v1.0
- [ ] Saved to `PRD.md` at project root
