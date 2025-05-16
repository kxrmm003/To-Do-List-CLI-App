# todo.py
# 📝 Simple To-Do List CLI App

def load_tasks():
    """Reads tasks from file and returns a list"""
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves the list of tasks to file"""
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    """Displays all tasks"""
    if not tasks:
        print("📭 No tasks founded.")
    else:
        print("\n📋 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

def add_task(tasks):
    """Adds a new task"""
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.\n")

def update_task(tasks):
    """Updates an existing task"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            new_task = input("Enter updated task: ")
            tasks[index] = new_task
            save_tasks(tasks)
            print("Task updated.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def delete_task(tasks):
    """Deletes a task by number"""
    show_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            save_tasks(tasks)
            print(f" Task '{deleted}' deleted.\n")
        else:
            print(" Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def main():
    print(" Welcome to the CLI To-Do List App")
    tasks = load_tasks()

    while True:
        print("Choose an option:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("EXIT")
            break
        else:
            print("⚠️ Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()

