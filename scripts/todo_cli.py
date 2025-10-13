# todo_cli.py

"""
Command-line Todo List Manager (CLI)

Lightweight and file-based todo list tool using only Python’s standard library.
Supports adding, listing, and removing tasks stored in a JSON file.
"""

import sys
import json
from pathlib import Path

# Define path for the todo list file
TODO_FILE = Path(__file__).parent / "todos.json"


def load_todos():
    """Load tasks from the JSON file, or return an empty list if it doesn’t exist."""
    if TODO_FILE.exists():
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_todos(todos):
    """Save the current list of tasks to the JSON file."""
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)


def list_todos():
    """Display all tasks with their index numbers."""
    todos = load_todos()
    if not todos:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todos, 1):
            print(f"{i}. {task}")


def add_task(task):
    """Add a new task to the todo list."""
    todos = load_todos()
    todos.append(task)
    save_todos(todos)
    print(f"Added: {task}")


def remove_task(index):
    """Remove a task by its index number."""
    todos = load_todos()
    try:
        removed = todos.pop(index - 1)
        save_todos(todos)
        print(f"Removed: {removed}")
    except IndexError:
        print("Invalid task number.")


def main():
    """Handle CLI arguments and execute the corresponding command."""
    if len(sys.argv) < 2:
        print("Usage: python todo_cli.py [add|list|remove] [task or index]")
        return

    command = sys.argv[1]

    # Match user command
    if command == "add":
        add_task(" ".join(sys.argv[2:]))  # Combine all remaining args as task name
    elif command == "list":
        list_todos()
    elif command == "remove":
        remove_task(int(sys.argv[2]))
    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
