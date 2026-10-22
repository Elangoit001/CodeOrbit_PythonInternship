"""Task 2: To-Do List CLI App
Add, view and remove tasks. Tasks are saved to tasks.txt.
"""

FILENAME = "tasks.txt"


def load_tasks():
    """Load tasks from the text file (empty list if file is missing)."""
    try:
        with open(FILENAME, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []


def save_tasks(tasks):
    """Save all tasks to the text file."""
    with open(FILENAME, "w") as f:
        for task in tasks:
            f.write(task + "\n")


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print(f"Added: '{task}'")
    else:
        print("Task cannot be empty.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks yet. Your list is empty!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


def remove_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: '{removed}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    tasks = load_tasks()
    print("=== To-Do List App ===")
    while True:
        print("\n1. Add task\n2. View tasks\n3. Remove task\n4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please pick 1-4.")


if __name__ == "__main__":
    main()