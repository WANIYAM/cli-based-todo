# Quickstart: Todo In-Memory Python Console Application

This guide provides instructions on how to set up and run the Todo application.

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
