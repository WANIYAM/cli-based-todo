# Data Model: Todo Application

This document defines the data entities for the Todo application, as required by the feature specification.

## Task Entity

The `Task` is the central entity in the application. It represents a single todo item.

### Fields

| Field         | Type    | Required | Description                                       | Constraints      |
|---------------|---------|----------|---------------------------------------------------|------------------|
| `id`          | Integer | Yes      | A unique, immutable identifier for the task.      | Must be unique.  |
| `title`       | String  | Yes      | A short, descriptive title for the task.          | Cannot be empty. |
| `description` | String  | No       | A more detailed description of the task.          | -                |
| `completed`   | Boolean | Yes      | The completion status of the task. Default `false`.| -                |

### State Transitions

A `Task` object has one primary state that can be transitioned: `completed`.

-   **Initial State**: When a task is created, the `completed` status is always `false` (incomplete).
-   **Transitions**: The `completed` status can be toggled from `false` to `true` (complete) and from `true` to `false` (incomplete) using the "Mark Task Complete / Incomplete" feature.

### Example

```json
{
  "id": 1,
  "title": "Implement the core logic",
  "description": "Write the service layer functions for adding, updating, and deleting tasks.",
  "completed": false
}
```
