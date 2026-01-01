from cli import CLITodoApp # Changed import

def main():
    """Main function to run the to-do application."""
    app = CLITodoApp() # Instantiated CLITodoApp directly
    app.run()

if __name__ == "__main__":
    main()