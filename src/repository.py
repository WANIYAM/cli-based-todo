from typing import Dict, List, Optional
from models import Task

class TaskRepository:
    """A repository for storing and managing tasks in memory."""

    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def add_task(self, title: str, description: str) -> Task:
        """Adds a new task to the repository."""
        task = Task(id=self._next_id, title=title, description=description)
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks from the repository."""
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Returns a task by its ID."""
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Optional[Task]:
        """Updates a task's title and/or description."""
        task = self.get_task_by_id(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
        return task

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by its ID."""
        if task_id in self._tasks:
            del self._tasks[task_id]
            return True
        return False

    def toggle_task_status(self, task_id: int) -> Optional[Task]:
        """Toggles a task's completed status."""
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = not task.completed
        return task
