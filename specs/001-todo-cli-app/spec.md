# Specification: Todo In-Memory Python Console Application (Phase I)

## Overview
This specification defines the functional and non-functional requirements for a command-line Todo application implemented in Python. The application stores all tasks in memory and supports basic task management operations. The goal is to demonstrate clean, spec-driven development using Spec-Kit Plus and Claude Code.
---
## System Context
- The system is a standalone CLI application.
- The user interacts via terminal commands or menu-driven prompts.
- All data exists only during runtime and is lost when the program exits.
- No external services, databases, or files are used.
---
## Actors
### Primary Actor
- **User**: A terminal user who manages todo tasks.
---
## Functional Requirements
### FR-1: Add Task
**Description:** The system shall allow the user to add a new todo task.
**Inputs:**
- Title (string, required, non-empty)
- Description (string, optional)
**Behavior:**
- The system generates a unique, immutable task ID.
- The task is stored in memory with status set to `incomplete`.
**Output:**
- Confirmation message displaying the task ID.
---
### FR-2: View Tasks
**Description:** The system shall display all existing tasks.
**Behavior:**
- Tasks are listed in a human-readable format.
- Each task displays:
  - ID
  - Title
  - Description
  - Status (Complete / Incomplete)
**Edge Cases:**
- If no tasks exist, the system displays an appropriate message.
---
### FR-3: Update Task
**Description:** The system shall allow the user to update an existing task.
**Inputs:**
- Task ID
- New title (optional)
- New description (optional)
**Behavior:**
- Only the title and/or description may be updated.
- Task ID remains unchanged.
- Status is preserved.
**Error Handling:**
- If the task ID does not exist, display an error message.
---
### FR-4: Delete Task
**Description:** The system shall allow the user to delete a task by ID.
**Inputs:**
- Task ID
**Behavior:**
- The task is removed from in-memory storage.
**Error Handling:**
- If the task ID does not exist, display an error message.
---
### FR-5: Mark Task Complete / Incomplete
**Description:** The system shall allow the user to toggle a task’s completion status.
**Inputs:**
- Task ID
**Behavior:**
- The task status is set to either `complete` or `incomplete`.
**Error Handling:**
- If the task ID does not exist, display an error message.
---
## Non-Functional Requirements
### NFR-1: In-Memory Storage
- All tasks must be stored only in memory.
- No file system or database persistence is allowed.
### NFR-2: Code Quality
- Code must be modular and readable.
- Clear separation between:
  - CLI interface
  - Domain logic
  - In-memory storage
### NFR-3: Compatibility
- The application must run on Python 3.13+.
- Must be executable via terminal using UV.
### NFR-4: User Experience
- Output must be clear and human-readable.
- Errors must be explicit and actionable.
---
## Data Model
### Task
A task is defined by:
- `id`: Unique, immutable identifier
- `title`: String
- `description`: String
- `completed`: Boolean
---
## Assumptions
- Single-user usage.
- Sequential interaction (no concurrency).
- IDs are generated internally and not user-defined.
---
## Acceptance Criteria
- All five basic features are implemented and functional.
- The application runs without errors.
- CLI output clearly demonstrates task lifecycle operations.
- Behavior matches this specification exactly.