# Tasks: Todo In-Memory Python Console Application

**Input**: Design documents from `specs/001-todo-cli-app/`
**Prerequisites**: plan.md, spec.md, data-model.md

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which functional requirement this task belongs to (e.g., FR1, FR2)

---

## Phase 1: Setup

**Purpose**: Project initialization and basic structure.

- [x] T001 [P] Create `pyproject.toml` for UV configuration.
- [x] T002 [P] Create the source directory `src/`.
- [x] T003 [P] Create empty file `src/main.py`.
- [x] T004 [P] Create empty file `src/cli.py`.
- [x] T005 [P] Create empty file `src/models.py`.
- [x] T006 [P] Create empty file `src/repository.py`.
- [x] T007 [P] Create empty file `src/services.py`.

---

## Phase 2: Foundational

**Purpose**: Core data model and storage mechanism.

- [x] T008 Implement the `Task` data class in `src/models.py` with fields: `id`, `title`, `description`, `completed`.
- [x] T009 Implement the `TaskRepository` class in `src/repository.py` with an in-memory dictionary to store tasks.

---

## Phase 3: Add Task (FR-1)

**Goal**: Allow a user to add a new task.
**Independent Test**: Run the app, add a task, and verify it's stored.

- [x] T010 [FR1] In `src/services.py`, implement a `create_task` function that takes a title and description, creates a `Task` object with a new unique ID, and adds it to the repository.
- [x] T011 [FR1] In `src/cli.py`, implement a function to prompt the user for a task title and description and call the `create_task` service.

---

## Phase 4: View Tasks (FR-2)

**Goal**: Allow a user to see all tasks.
**Independent Test**: Run the app, add a few tasks, view them, and verify the output is correct.

- [x] T012 [FR2] In `src/services.py`, implement a `get_all_tasks` function that returns all tasks from the repository.
- [x] T013 [FR2] In `src/cli.py`, implement a function to display all tasks in a human-readable format. Handle the case where there are no tasks.

---

## Phase 5: Update Task (FR-3)

**Goal**: Allow a user to update a task's title and description.
**Independent Test**: Run the app, add a task, update it, view it again, and verify the changes.

- [x] T014 [FR3] In `src/services.py`, implement an `update_task` function that takes a task ID, and optional new title and description, and updates the task in the repository.
- [x] T015 [FR3] In `src/cli.py`, implement a function to prompt the user for a task ID and the new details, then call the `update_task` service.

---

## Phase 6: Delete Task (FR-4)

**Goal**: Allow a user to delete a task.
**Independent Test**: Run the app, add a task, delete it, view tasks, and verify it's gone.

- [x] T016 [FR4] In `src/services.py`, implement a `delete_task` function that takes a task ID and removes the task from the repository.
- [x] T017 [FR4] In `src/cli.py`, implement a function to prompt the user for a task ID to delete and call the `delete_task` service.

---

## Phase 7: Mark Task Complete/Incomplete (FR-5)

**Goal**: Allow a user to change a task's completion status.
**Independent Test**: Run the app, add a task, mark it complete, view it, and verify the status has changed.

- [x] T018 [FR5] In `src/services.py`, implement a `toggle_task_status` function that takes a task ID and flips its `completed` status.
- [x] T019 [FR5] In `src/cli.py`, implement a function to prompt the user for a task ID and call the `toggle_task_status` service.

---

## Phase 8: Integration

**Purpose**: Connect all the pieces into a working application.

- [x] T020 In `src/main.py`, implement the main application loop that shows a menu of options, gets user input, and calls the appropriate functions from `src/cli.py`.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation and cleanup.

- [x] T021 [P] Create `README.md` with setup and usage instructions.
- [x] T022 [P] Create `CLAUDE.md` with instructions for using AI assistance.

---

## Dependencies & Execution Order

- **Phase 1 (Setup)** must be completed first.
- **Phase 2 (Foundational)** depends on Phase 1.
- **Phases 3-7 (Functional Requirements)** depend on Phase 2. They can largely be implemented in parallel after Phase 2 is done.
- **Phase 8 (Integration)** depends on all previous phases.
- **Phase 9 (Polish)** can be done in parallel with other phases.
