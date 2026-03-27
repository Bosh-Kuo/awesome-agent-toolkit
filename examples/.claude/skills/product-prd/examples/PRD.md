# FocusFlow — Product Requirements Document

> **Version:** 0.1 | **Date:** 2026-03-25 | **Status:** Draft

---

## 1. Project Overview

- **One-sentence description:** A productivity web app that helps remote workers focus on daily tasks and track deep work time.
- **Core Problem:** Remote workers frequently switch between multiple projects and lack a unified place to manage "what to do today" and "how much time was actually spent." Existing tools (Notion, Todoist) are too bloated and add cognitive load.
- **Target Audience (TA):** Remote software engineers, freelancers, solopreneurs.

---

## 2. Product Vision

> We want **remote workers** to be able to **plan their day and stay in flow** so that **they end each day knowing exactly what they accomplished**.

---

## 3. Core Objectives

- [ ] Users can complete their daily task planning within 2 minutes.
- [ ] Weekly deep work time statistics are generated automatically without manual tracking.
- [ ] Reach 500 weekly active users within 3 months after MVP launch.

---

## 4. User Personas

### Busy Remote Engineer (Alex)
- **Goal:** Quickly decide "what to finish today" before starting work and know how much was done before logging off.
- **Pain Point:** Notion is too complex; hard to regain flow after meeting interruptions; doesn't know where the time went.

### Multi-project Freelancer (Sam)
- **Goal:** Track time spent on different client projects for easier end-of-month invoicing.
- **Pain Point:** Currently using spreadsheets for manual tracking, which is easy to forget and leads to incomplete data.

---

## 5. Key Feature Groups

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

## 6. System Architecture Overview

- **Platform / Tech Stack:**
  - Frontend: Next.js (App Router) + Tailwind CSS
  - Backend: Next.js API Routes + Prisma ORM
  - Database: PostgreSQL (hosted on Supabase)
  - Infra: Vercel (frontend + API)
- **Key Components:**
  - `TaskService` — Task CRUD and daily reset logic
  - `TimerService` — Timer state management and task record integration
  - `StatsEngine` — Aggregating work time and completion rate statistics
- **External Integrations:** Google OAuth (NextAuth.js), Supabase (DB + Auth alternative)

---

## 7. Out of Scope

- Not supporting multiplayer collaboration and task assignment (evaluate in v2)
- No Native Mobile App initially, responsive web only
- No AI smart scheduling or automated priority suggestions
- No integration with external tools like Slack or Jira (evaluate in v2)

---

## 8. Phased Roadmap

| Phase | Goal | Key Features |
|------|------|---------|
| MVP | Validate daily tasks + timer core loop | Task management, Pomodoro timer, basic authentication |
| v1.0 | Complete launchable product | Stats dashboard, tagging system, task retention logic |
| v2.0 | Expand use cases | Mobile PWA, team features, third-party integrations |

---

## 9. Success Metrics

- Reach 500 weekly active users within 3 months of MVP launch
- 60% of active users use the timer feature daily
- Average time for users to complete daily planning is < 2 minutes
- 30-day user retention rate > 40%

---

## 10. Open Questions

- [ ] Does timer data need to support export (CSV / PDF)?
- [ ] Should we support multiple "project" categories in the MVP, or use tags as a substitute initially?
- [ ] Where should we draw the feature boundary between the free and paid plans?
