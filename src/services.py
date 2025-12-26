from repository import TaskRepository
from models import Task

class TaskService:
    """Service layer for managing tasks."""

    def __init__(self, repository: TaskRepository):
        self._repository = repository

    def create_task(self, title: str, description: str) -> Task:
        """Creates a new task."""
        if not title:
            raise ValueError("Title cannot be empty.")
        return self._repository.add_task(title, description)

    def get_all_tasks(self):
        """Returns all tasks."""
        return self._repository.get_all_tasks()

    def update_task(self, task_id: int, title: str = None, description: str = None):
        """Updates a task."""
        task = self._repository.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        return self._repository.update_task(task_id, title, description)

    def delete_task(self, task_id: int):
        """Deletes a task."""
        task = self._repository.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        return self._repository.delete_task(task_id)

    def toggle_task_status(self, task_id: int):
        """Toggles a task's status."""
        task = self._repository.get_task_by_id(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found.")
        return self._repository.toggle_task_status(task_id)
