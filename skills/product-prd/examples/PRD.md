# FocusFlow — Product Requirements Document

> **Date:** 2026-03-25 | **Status:** Draft | **Current Phase:** v0.2

---

## 1. Project Overview

- **One-sentence description:** A productivity web app that helps remote workers focus on daily tasks and track deep work time.
- **Product Vision:** Help remote workers plan their day, stay in flow, and end each workday with a clear record of what they accomplished.
- **Core Problem:** Remote workers frequently switch between multiple projects and lack a unified place to manage "what to do today" and "how much time was actually spent." Existing tools (Notion, Todoist) are too bloated and add cognitive load.
- **Target Audience (TA):** Remote software engineers, freelancers, solopreneurs.
- **Current Product Phase:** v0.2 — refine the validated MVP with a small group of recurring users before preparing for a broader launch.

---

## 2. Core Objectives

- Users can complete daily task planning within 2 minutes.
- Users can track deep work time without manual spreadsheet entry.
- Users can review weekly task completion and focus-time patterns from one dashboard.

---

## 3. User Personas

### Busy Remote Engineer (Alex)
- **Goal:** Quickly decide "what to finish today" before starting work and know how much was done before logging off.
- **Pain Point:** Notion is too complex; hard to regain flow after meeting interruptions; doesn't know where the time went.

### Multi-project Freelancer (Sam)
- **Goal:** Track time spent on different client projects for easier end-of-month invoicing.
- **Pain Point:** Currently using spreadsheets for manual tracking, which is easy to forget and leads to incomplete data.

---

## 4. Key Feature Groups

1. **User Authentication**
   - Email/Password registration and login
   - Google OAuth one-click login

2. **Daily Task Board**
   - Create, edit, complete, and delete tasks
   - Support for priority tags (High / Medium / Low)
   - Daily task list resets automatically at midnight (unfinished tasks can be retained optionally)

3. **Focus Timer**
   - Pomodoro mode (25 mins work / 5 mins rest)
   - Customizable work and rest durations
   - Timer linked to tasks automatically, recording actual work time for each task

4. **Stats Dashboard**
   - Number of completed tasks this week / this month
   - Deep work time statistics (filterable by project or tag)

---

## 5. Tech Stack

- **Platform:** Responsive web app
- **Language / Runtime:** TypeScript + Node.js
- **Frontend Framework:** Next.js App Router
- **UI / Component System:** shadcn/ui + Radix UI primitives
- **Styling:** Tailwind CSS
- **Backend / API:** Next.js API Routes
- **Database:** PostgreSQL hosted on Supabase
- **ORM / Data Access:** Prisma
- **Authentication:** Better Auth with Google OAuth and email/password fallback
- **Forms / Validation:** React Hook Form + Zod
- **Background Jobs / Queue:** Scheduled jobs for daily rollover and weekly summary generation
- **Infrastructure / Hosting:** Vercel for application hosting; Supabase for managed database
- **Observability / Analytics:** Application logging and basic product analytics
- **External Integrations:** Google OAuth; no productivity-tool integrations in the current phase

---

## 6. System Architecture Overview

- **Client / Interface:** Responsive web app for daily planning, timer control, and dashboard review.
- **Application Layer:** API layer for account access, task management, timer sessions, and dashboard data.
- **Data Store:** Primary relational database for users, tasks, projects/tags, timer sessions, and weekly aggregates.
- **Background Processing:** Scheduled jobs for daily task rollover and weekly summary generation.
- **Cache / Search:** Not needed for the v0.2 phase.
- **Observability:** Application logging and basic usage analytics for core workflow completion and timer usage.
- **External Integrations:** Google OAuth for sign-in; no third-party productivity tool integrations in the current phase.

---

## 7. Phased Roadmap

| Phase | Status | Goal | Key Features / Scope | Future Work / Out of Scope Notes |
|------|--------|------|----------------------|----------------------------------|
| v0.1 | Completed | Validate the daily task board + focus timer core loop. | Basic authentication, daily task board, Pomodoro timer, task-linked time records, basic weekly dashboard. | Team collaboration, native mobile app, AI scheduling, and third-party productivity integrations were intentionally excluded. |
| v0.2 | Current | Improve retention and workflow clarity for recurring solo users. | Task retention preferences, project/tag filtering, weekly dashboard improvements, onboarding copy refinements, CSV export for freelancer reporting. | No team workspace, native mobile app, AI scheduling, Slack/Jira integration, or billing system in this phase. |
| Future Work | Future Work | Expand FocusFlow beyond the validated solo remote-worker workflow. | Team workspaces, shared task boards, Slack/Jira integrations, AI-assisted scheduling, native mobile app, paid plan and billing flows. | All items here are deferred until v0.2 retention and workflow clarity are validated. |
