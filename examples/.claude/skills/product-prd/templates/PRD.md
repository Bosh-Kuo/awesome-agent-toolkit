# [Product Name] — Product Requirements Document

> **Date:** [YYYY-MM-DD] | **Status:** Draft | **Current Phase:** [Current phase name, e.g., v0.2]

---

## 1. Project Overview

- **One-sentence description:** [Use one sentence to describe what this product does and who it is for]
- **Product Vision:** [Use one sentence to describe what transformative outcome this product enables for the target audience]
- **Core Problem:** [Describe the pain point users currently face and why existing solutions are insufficient]
- **Target Audience (TA):** [Primary user groups, e.g., remote workers, small e-commerce sellers, software engineers]
- **Current Product Phase:** [Name the current phase, e.g., v0.2, and summarize what the project is trying to complete now]

---

## 2. Core Objectives

> Use product-level objectives. Avoid TODO checkboxes and implementation tasks.

- [Objective 1: concrete product outcome]
- [Objective 2: concrete product outcome]
- [Objective 3: concrete product outcome]

---

## 3. User Personas

### [Persona 1 Name, e.g., Busy Entrepreneur]
- **Goal:** [What they want to achieve]
- **Pain Point:** [What currently bothers them]

### [Persona 2 Name]
- **Goal:** [What they want to achieve]
- **Pain Point:** [What currently bothers them]

---

## 4. Key Feature Groups

> List high-level feature groups here, **not** detailed specifications for individual features. For individual feature specs, use the spec-writer tool.

1. **[Group Name, e.g., User Authentication]**
   - [Capability description, e.g., Email/Password registration and login]
   - [Capability description, e.g., Google / GitHub OAuth]

2. **[Group Name, e.g., Core Workflow]**
   - [Capability description]
   - [Capability description]

3. **[Group Name]**
   - [Capability description]
   - [Capability description]

---

## 5. Tech Stack

- **Platform:** [Web app, mobile app, desktop app, CLI, API service, or TBD]
- **Language / Runtime:** [TypeScript, Node.js, Python, etc., or TBD]
- **Frontend Framework:** [Framework, routing mode, rendering model, or TBD]
- **UI / Component System:** [shadcn/ui, Radix UI, Material UI, custom design system, or TBD]
- **Styling:** [Tailwind CSS, CSS Modules, styled-components, etc., or TBD]
- **Backend / API:** [Runtime / server framework / API approach, or TBD]
- **Database:** [Primary database, or TBD]
- **ORM / Data Access:** [Prisma, Drizzle, SQLAlchemy, etc., or TBD]
- **Authentication:** [Better Auth, NextAuth.js, Auth0, custom auth, or TBD]
- **Forms / Validation:** [React Hook Form, Zod, Yup, etc., or TBD]
- **Background Jobs / Queue:** [BullMQ, Inngest, message queue, scheduled jobs, or Not Needed]
- **Infrastructure / Hosting:** [Hosting, deployment, storage, CDN, or TBD]
- **Observability / Analytics:** [Logging, monitoring, product analytics, or TBD]
- **External Integrations:** [Third-party services to integrate, or None]

---

## 6. System Architecture Overview

> List key system components and their responsibilities. Do not list feature-specific modules unless they are genuine architecture components.

- **Client / Interface:** [Primary user-facing app, admin console, CLI, API client, or TBD]
- **Application Layer:** [Backend/API/server layer responsibilities, or TBD]
- **Data Store:** [Primary persistence layer and what it stores, or TBD]
- **Background Processing:** [Message queue, workers, scheduled jobs, or Not Needed]
- **Cache / Search:** [Cache, search index, or Not Needed]
- **Observability:** [Logging, monitoring, analytics, alerting, or TBD]
- **External Integrations:** [Third-party services to integrate, or None]

---

## 7. Phased Roadmap

> Mark exactly one current phase. Include prior phases when useful. Put all later goals in one consolidated Future Work phase.

| Phase | Status | Goal | Key Features / Scope | Future Work / Out of Scope Notes |
|------|--------|------|----------------------|----------------------------------|
| [Completed phase name, e.g., v0.1] | Completed | [What this phase achieved] | [Capabilities already completed] | [Optional notes] |
| [Current phase name, e.g., v0.2] | Current | [What this phase must achieve] | [2-5 capabilities in current scope] | [Explicit exclusions for the current phase] |
| Future Work | Future Work | [All goals intentionally deferred until after the current phase] | [All deferred capabilities grouped here] | [Clarify that these items are not part of the current phase] |
