from services import TaskService

class CLI:
    """Command-line interface for the to-do application."""

    def __init__(self, service: TaskService):
        self._service = service

    def _display_menu(self):
        """Displays the main menu."""
        print("\n--- To-Do List Menu ---")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Update a task")
        print("4. Delete a task")
        print("5. Mark a task as complete/incomplete")
        print("6. Exit")

    def run(self):
        """Runs the main application loop."""
        while True:
            self._display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                self._add_task()
            elif choice == '2':
                self._view_tasks()
            elif choice == '3':
                self._update_task()
            elif choice == '4':
                self._delete_task()
            elif choice == '5':
                self._toggle_task_status()
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

    def _add_task(self):
        """Handles adding a new task."""
        try:
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            task = self._service.create_task(title, description)
            print(f"Task '{task.title}' added with ID {task.id}.")
        except ValueError as e:
            print(f"Error: {e}")

    def _view_tasks(self):
        """Handles viewing all tasks."""
        tasks = self._service.get_all_tasks()
        if not tasks:
            print("No tasks found.")
        else:
            print("\n--- All Tasks ---")
            for task in tasks:
                status = "Complete" if task.completed else "Incomplete"
                print(f"ID: {task.id}, Title: {task.title}, Description: {task.description}, Status: {status}")

    def _update_task(self):
        """Handles updating a task."""
        try:
            task_id = int(input("Enter task ID to update: "))
            title = input("Enter new title (or press Enter to skip): ")
            description = input("Enter new description (or press Enter to skip): ")
            self._service.update_task(task_id, title if title else None, description if description else None)
            print(f"Task {task_id} updated.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please enter a valid task ID.")

    def _delete_task(self):
        """Handles deleting a task."""
        try:
            task_id = int(input("Enter task ID to delete: "))
            self._service.delete_task(task_id)
            print(f"Task {task_id} deleted.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please enter a valid task ID.")

    def _toggle_task_status(self):
        """Handles toggling a task's status."""
        try:
            task_id = int(input("Enter task ID to toggle status: "))
            task = self._service.toggle_task_status(task_id)
            status = "Complete" if task.completed else "Incomplete"
            print(f"Task {task.id} status changed to {status}.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception:
            print("Invalid input. Please enter a valid task ID.")
