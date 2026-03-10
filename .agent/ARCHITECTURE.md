# Antigravity Kit Architecture

> Comprehensive AI Agent Capability Expansion Toolkit

---

## 📋 Overview

Antigravity Kit is a modular system consisting of:

- **3 Specialist Agents** - Role-based AI personas
- **22 Skills** - Domain-specific knowledge modules
- **1 Workflows** - Slash command procedures

---

## 🏗️ Directory Structure

```plaintext
.agent/
├── ARCHITECTURE.md          # This file
├── agents/                  # 3 Specialist Agents
├── skills/                  # 22 Skills
├── workflows/               # 1 Slash Commands
├── rules/                   # Global Rules
└── scripts/                 # Master Validation Scripts
```

---

## 🤖 Agents (3)

Specialist AI personas for different domains.

| Agent                    | Focus                      | Skills Used                                              |
| ------------------------ | -------------------------- | -------------------------------------------------------- |
| `frontend-specialist`    | Web UI/UX                  | frontend-design, react-components, tailwind-patterns     |
| `backend-specialist`     | API, business logic        | supabase-postgres-best-practices, postgres-patterns      |
| `qa-automation-engineer` | E2E testing, CI pipelines  | lint-and-validate, playwright-cli, agent-browser         |

---

## 🧩 Skills (22)

Modular knowledge domains that agents can load on-demand based on task context.

### Frontend & UI

| Skill                    | Description                                                           |
| ------------------------ | --------------------------------------------------------------------- |
| `frontend-design`        | UI/UX patterns, design systems                                        |
| `tailwind-patterns`      | Tailwind CSS v4 patterns & utilities                                  |
| `react-components`       | Converts Stitch designs into modular Vite/React components            |
| `shadcn-ui`              | Expert guidance for integrating and building with shadcn/ui           |
| `web-design-guidelines`  | Web UI audit context - rules for accessibility, UX, and performance   |
| `pwa-manifest-generator` | Generate PWA manifests for frontend development                       |

### Frameworks & Libraries

| Skill                 | Description                                                  |
| --------------------- | ------------------------------------------------------------ |
| `nextjs-react-expert` | React & Next.js performance optimization & best practices    |
| `vite`                | Vite build tool configuration, plugin API, SSR               |
| `remotion`            | Generate walkthrough videos with smooth transitions          |

### Backend & Database

| Skill                              | Description                                         |
| ---------------------------------- | --------------------------------------------------- |
| `postgres-patterns`                | PostgreSQL database patterns for query optimization |
| `supabase-postgres-best-practices` | Postgres performance and best practices (Supabase)  |
| `rust-pro`                         | Master Rust with async patterns & production setup  |

### AI, Layout & Prototyping

| Skill                   | Description                                                 |
| ----------------------- | ----------------------------------------------------------- |
| `cms-tour-mapping`      | Map Google Drive PDF sales info into the Happybook CMS      |
| `design-md`             | Analyze Stitch projects to synthesize a design system       |
| `stitch-loop`           | Iteratively build websites using Stitch with an auto loop   |
| `enhance-prompt`        | Transforms vague UI ideas into polished, precise prompts    |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component UIs  |

### Architecture & Tools

| Skill               | Description                               |
| ------------------- | ----------------------------------------- |
| `agent-browser`     | Browser automation CLI for AI agents      |
| `app-builder`       | Main application building orchestrator    |
| `google-drive`      | Google Drive API integration              |
| `lint-and-validate` | Code linting, formatting, validation      |
| `playwright-cli`    | Automates browser interactions & testing  |

---

## 🔄 Workflows (1)

Slash command procedures. Invoke with `/command`.

| Command        | Description              |
| -------------- | ------------------------ |
| `/orchestrate` | Multi-agent coordination |

---

## 🎯 Skill Loading Protocol

```plaintext
User Request → Skill Description Match → Load SKILL.md
                                            ↓
                                    Read references/
                                            ↓
                                    Read scripts/
```

### Skill Structure

```plaintext
skill-name/
├── SKILL.md           # (Required) Metadata & instructions
├── scripts/           # (Optional) Python/Bash scripts
├── references/        # (Optional) Templates, docs
└── assets/            # (Optional) Images, logos
```

---

## 📊 Statistics

| Metric              | Value                         |
| ------------------- | ----------------------------- |
| **Total Agents**    | 3                             |
| **Total Skills**    | 22                            |
| **Total Workflows** | 1                             |

---

## 🔗 Quick Reference

| Need     | Agent                    | Skills                                             |
| -------- | ------------------------ | -------------------------------------------------- |
| Web App  | `frontend-specialist`    | nextjs-react-expert, frontend-design, shadcn-ui    |
| Backend  | `backend-specialist`     | supabase-postgres-best-practices, rust-pro         |
| Testing  | `qa-automation-engineer` | lint-and-validate, playwright-cli, agent-browser   |
