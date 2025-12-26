---
id: 1
title: Define Project Constitution and Principles
stage: constitution
date: 2025-12-26
surface: agent
model: gemini-pro
feature: none
branch: main
user: N/A
command: /sp.constitution
labels: [constitution, principles]
links:
  spec: "null"
  ticket: "null"
  adr: "null"
  pr: "null"
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - None
---

## Prompt

/sp.constitution # Todo In-Memory Python Console Application (Phase I)

## Project Initialization
The project shall be initialized using Spec-Kit Plus and Claude Code with the following steps:

1. Initialize the repository using Spec-Kit Plus.
2. Ensure the repository is tracked with Git from the beginning.
3. Use UV for Python environment and dependency management.
4. Target Python version 3.13 or higher.
5. Establish the following baseline structure:
   - `src/` for all Python source code
   - `specs/history/` for all generated specification artifacts
   - `README.md` for setup and usage instructions
   - `CLAUDE.md` for Claude Code usage guidance
6. All development must follow spec-driven development:
   - Constitution → Specification → Plan → Tasks → Implementation
7. No implementation work may begin before specifications are approved.

---

## Purpose
Build a clean, reliable, command-line Todo application that stores tasks entirely in memory and demonstrates spec-driven development using Spec-Kit Plus and Claude Code. The project must satisfy all Phase I hackathon requirements and serve as a foundation for future evolution phases.

---

## Scope
The application will:
- Run entirely in the terminal
- Manage todo tasks in memory only (no persistence)
- Support all five basic CRUD-related operations
- Be implemented using Python 3.13+
- Follow spec-driven development strictly using Spec-Kit Plus

Out of scope:
- File-based storage
- Databases
- GUI or web interfaces
- Authentication or user roles
- External APIs

---

## Core Features (Phase I – Basic Level)
1. Add a task with:
   - Title
   - Description
2. View all tasks with:
   - Unique immutable ID
   - Title
   - Description
   - Completion status (complete / incomplete)
3. Update task title and description by ID
4. Delete a task by ID
5. Mark a task as complete or incomplete by ID

---

## Principles
- Spec-first, implementation second
- Clear separation of concerns (CLI, domain logic, storage)
- No global mutable state
- Immutable task IDs
- In-memory storage only
- Predictable and human-readable CLI output
- Simple, explicit control flow
- Fail fast with clear error messages
- Clean code and readable structure over cleverness

---

## Constraints
- Python version: 3.13 or higher
- Console-based interaction only
- No external databases or file persistence
- Use Spec-Kit Plus for all specs and planning
- Use Claude Code as the AI coding assistant
- Must be runnable via terminal using UV
- Must conform to hackathon Phase I requirements exactly

---

## Success Criteria
The project is successful when:
- All five basic features are fully functional
- The application runs without errors using UV
- Specs clearly describe behavior and match implementation
- Code is modular, readable, and maintainable
- Repository structure matches deliverables exactly
- The console demo clearly shows all required operations

---

## Non-Goals
- Performance optimization
- Persistence or scalability
- Advanced CLI frameworks
- Unit testing (unless explicitly added later)

## Response snapshot

The project constitution has been updated to version 1.0.0, incorporating the nine principles provided. The plan template has been synchronized with these principles to ensure alignment in future development planning. A Prompt History Record (PHR) has been created to document this action.

## Outcome

- ✅ Impact: The project's guiding principles are now formally documented in `.specify/memory/constitution.md` and integrated into the planning template.
- 🧪 Tests: No tests were run.
- 📁 Files: Modified `.specify/memory/constitution.md` and `.specify/templates/plan-template.md`. Created `history/prompts/constitution/1-define-project-constitution-and-principles.constitution.prompt.md`.
- 🔁 Next prompts: The user can now proceed with defining the specification using `/sp.specify`.
- 🧠 Reflection: The initial user prompt contained the full project definition, but the `/sp.constitution` command correctly extracted and applied only the principles to the constitution file. The git repository was not initialized, which caused a minor issue when trying to get the branch name.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
