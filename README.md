# Todo In-Memory Python Console Application

This is a simple, in-memory command-line to-do application built in Python. It is designed to demonstrate spec-driven development using Spec-Kit Plus.

## Prerequisites

- Python 3.13 or higher
- [UV](https://github.com/astral-sh/uv) installed

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd todo-evolution
    ```

2.  **Create a virtual environment using UV:**
    ```bash
    uv venv
    ```

3.  **Activate the virtual environment:**
    -   **Windows (PowerShell):**
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    -   **macOS/Linux:**
        ```bash
        source .venv/bin/activate
        ```

## Running the Application

Once the virtual environment is activated, you can run the application with the following command:

```bash
uv run python src/main.py
```

The application will start, and you will see the main menu, from which you can manage your todo tasks.

## Features

- Add a new task
- View all tasks
- Update an existing task
- Delete a task
- Mark a task as complete or incomplete
