# src/cli.py
from services import TaskService
from repository import TaskRepository # Added import

def _print_header(title: str):
    """Prints a formatted header."""
    line = "=" * (len(title) + 4)
    print(f"\n{line}")
    print(f"= {title} =")
    print(f"{line}\n")

def _print_menu():
    """Prints the main menu."""
    _print_header("Main Menu")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Toggle task status (Complete/Incomplete)") # Modified menu item
    print("4. Delete a task") # Re-numbered
    print("5. Exit") # Re-numbered
    print("-" * 20)

def _display_tasks(tasks):
    """Displays a list of tasks in a clean, table-like format."""
    _print_header("Your Tasks")
    if not tasks:
        print("No tasks found. Add one from the menu!")
        return

    # Determine maximum lengths for dynamic column widths
    max_id_len = len(str(max(t.id for t in tasks))) if tasks else 2
    max_title_len = len(max((t.title for t in tasks), key=len)) if tasks else 5
    max_description_len = len(max((t.description for t in tasks), key=len)) if tasks else 11

    # Ensure minimum width for Title and Description
    max_title_len = max(max_title_len, len("Title"))
    max_description_len = max(max_description_len, len("Description"))
    
    # Header
    id_col = "ID".ljust(max_id_len)
    status_col = "Status".ljust(7) # "[✓]" is 3 chars, "[ ]" is 3 chars, plus padding
    title_col = "Title".ljust(max_title_len)
    desc_col = "Description".ljust(max_description_len) # Adjusted for dynamic width
    
    # Calculate total width for separator line
    total_width = max_id_len + 7 + max_title_len + max_description_len + 9 # 3 pipes + 6 spaces
    
    print(f"{id_col} | {status_col} | {title_col} | {desc_col}")
    print("-" * total_width)

    # Rows
    for task in tasks:
        status_symbol = "[✓]" if task.completed else "[ ]" # Changed to task.completed
        id_str = str(task.id).ljust(max_id_len)
        status_str = status_symbol.ljust(7) # Adjusted for consistent width
        title_str = task.title.ljust(max_title_len)
        description_str = task.description.ljust(max_description_len) # Adjusted for dynamic width
        print(f"{id_str} | {status_str} | {title_str} | {description_str}")

class CLITodoApp:
    def __init__(self):
        self.repository = TaskRepository() # Instantiated TaskRepository
        self.service = TaskService(repository=self.repository) # Passed repository to TaskService

    def run(self):
        _print_header("Welcome to Your CLI Todo App")
        while True:
            _print_menu()
            choice = input("Enter your choice: ")
            try:
                if choice == "1":
                    self._add_task()
                elif choice == "2":
                    self._view_tasks()
                elif choice == "3": # Modified choice handling
                    self._toggle_task_status()
                elif choice == "4": # Re-numbered
                    self._delete_task()
                elif choice == "5": # Re-numbered
                    print("\nGoodbye!\n")
                    break
                else:
                    print("\n[Error] Invalid choice. Please try again.")
            except ValueError as ve:
                print(f"\n[Error] Invalid input: {ve}")
            except Exception as e:
                print(f"\n[Error] An unexpected error occurred: {e}")

    def _add_task(self):
        _print_header("Add a New Task")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        if not title:
            print("\n[Error] Title cannot be empty.")
            return
        task = self.service.create_task(title, description) # Changed to create_task
        print(f"\n[Success] Task '{task.title}' added with ID {task.id}.")

    def _view_tasks(self):
        tasks = self.service.get_all_tasks() # Changed to get_all_tasks
        _display_tasks(tasks)

    def _toggle_task_status(self): # New method for toggling status
        self._view_tasks()
        try:
            task_id_str = input("\nEnter the ID of the task to toggle its status: ")
            task_id = int(task_id_str)
            updated_task = self.service.toggle_task_status(task_id)
            if updated_task:
                status = "completed" if updated_task.completed else "incomplete"
                print(f"\n[Success] Task {task_id} status toggled to {status}.")
            else:
                print(f"\n[Error] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[Error] Invalid ID. Please enter a number.")

    def _delete_task(self):
        self._view_tasks()
        try:
            task_id_str = input("\nEnter the ID of the task to delete: ")
            task_id = int(task_id_str)
            if self.service.delete_task(task_id): # Changed to delete_task
                print(f"\n[Success] Task {task_id} deleted.")
            else:
                print(f"\n[Error] Task with ID {task_id} not found.")
        except ValueError:
            print("\n[Error] Invalid ID. Please enter a number.")

if __name__ == "__main__":
    app = CLITodoApp()
    app.run()
