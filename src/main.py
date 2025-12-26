from cli import CLI
from repository import TaskRepository
from services import TaskService

def main():
    """Main function to run the to-do application."""
    repository = TaskRepository()
    service = TaskService(repository)
    cli = CLI(service)
    cli.run()

if __name__ == "__main__":
    main()
