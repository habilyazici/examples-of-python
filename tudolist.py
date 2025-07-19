import os
import time
import datetime

TASKS_FILE = "tasks.txt"
ENCODING = "utf-8"

def load_tasks():
    """Load tasks from file. Each task is a dict."""
    tasks = []
    if not os.path.exists(TASKS_FILE):
        return tasks
    try:
        with open(TASKS_FILE, "r", encoding=ENCODING) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                # Format: description|completed|priority|due_date
                parts = line.split("|")
                if len(parts) != 4:
                    continue
                description, completed, priority, due_date = parts
                tasks.append({
                    "description": description,
                    "completed": completed == "True",
                    "priority": int(priority),
                    "due_date": due_date
                })
    except Exception as e:
        print(f"Error reading file: {e}")
    return tasks

def save_tasks(tasks):
    """Save tasks to file."""
    try:
        with open(TASKS_FILE, "w", encoding=ENCODING) as f:
            for task in tasks:
                line = f"{task['description']}|{task['completed']}|{task['priority']}|{task['due_date']}\n"
                f.write(line)
    except Exception as e:
        print(f"Error writing file: {e}")

def list_tasks(tasks):
    """List all tasks."""
    if not tasks:
        print("\nNo tasks found.\n")
        return
    print("\nYour Tasks:")
    for idx, task in enumerate(tasks, 1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{idx}. [{status}] (Priority: {task['priority']}) (Due: {task['due_date']}) - {task['description']}")
    print()

def add_task(tasks):
    """Add a new task."""
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty!")
        return
    try:
        priority = int(input("Enter priority (1-5, 1=highest): ").strip())
        if priority < 1 or priority > 5:
            print("Priority must be between 1 and 5.")
            return
    except ValueError:
        print("Priority must be a number.")
        return
    due_date = input("Enter due date (YYYY-MM-DD) or leave blank: ").strip()
    if due_date:
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return
    else:
        due_date = "No due date"
    tasks.append({
        "description": description,
        "completed": False,
        "priority": priority,
        "due_date": due_date
    })
    save_tasks(tasks)
    print("Task added successfully.")

def delete_task(tasks):
    """Delete a task by its number."""
    if not tasks:
        print("No tasks to delete.")
        return
    list_tasks(tasks)
    try:
        idx = int(input("Enter the task number to delete: ").strip())
        if idx < 1 or idx > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    deleted = tasks.pop(idx - 1)
    save_tasks(tasks)
    print(f"Task '{deleted['description']}' deleted.")

def edit_task(tasks):
    """Edit a task by its number."""
    if not tasks:
        print("No tasks to edit.")
        return
    list_tasks(tasks)
    try:
        idx = int(input("Enter the task number to edit: ").strip())
        if idx < 1 or idx > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    task = tasks[idx - 1]
    print(f"Editing task: {task['description']}")
    new_description = input("Enter new description (leave blank to keep current): ").strip()
    if new_description:
        task["description"] = new_description
    try:
        new_priority = input("Enter new priority (1-5, leave blank to keep current): ").strip()
        if new_priority:
            new_priority = int(new_priority)
            if new_priority < 1 or new_priority > 5:
                print("Priority must be between 1 and 5.")
                return
            task["priority"] = new_priority
    except ValueError:
        print("Priority must be a number.")
        return
    new_due_date = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ").strip()
    if new_due_date:
        try:
            datetime.datetime.strptime(new_due_date, "%Y-%m-%d")
            task["due_date"] = new_due_date
        except ValueError:
            print("Invalid date format.")
            return
    save_tasks(tasks)
    print("Task updated.")

def toggle_task_completion(tasks):
    """Mark a task as completed or not completed."""
    if not tasks:
        print("No tasks to update.")
        return
    list_tasks(tasks)
    try:
        idx = int(input("Enter the task number to toggle completion: ").strip())
        if idx < 1 or idx > len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    tasks[idx - 1]["completed"] = not tasks[idx - 1]["completed"]
    save_tasks(tasks)
    print("Task status updated.")

def main_menu():
    """Main menu loop."""
    tasks = load_tasks()
    while True:
        print("==== TO-DO LIST MENU ====")
        print("1. List tasks")
        print("2. Add new task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Toggle task completion")
        print("6. Exit")
        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            edit_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            toggle_task_completion(tasks)
        elif choice == "6":
            print("Exiting... Goodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid selection. Please try again.")
        time.sleep(1)

if __name__ == "__main__":
    main_menu()
