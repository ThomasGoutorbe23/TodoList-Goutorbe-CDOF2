# Python console application for a To-Do list

import json
import os

DATA_FILE = "data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DATA_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(title, description="", priority="Medium"):
    tasks = load_tasks()
    task = {
        "title": title,
        "description": description,
        "completed": False,
        "priority": priority
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' deleted successfully!")
    else:
        print("Invalid task index.")

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['title']}' marked as completed!")
    else:
        print("Invalid task index.")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks):
        if "priority" not in task:
            task["priority"] = "Medium"  
        status = "Completed" if task["completed"] else "Not completed"
        print(f"{index}. [{status}] [Priority: {task['priority']}] {task['title']} - {task['description']}")
    save_tasks(tasks)  
    
def main():
    while True:
        print("\nTodo List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Complete Task")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            print("Select priority level:")
            print("1. Low")
            print("2. Medium")
            print("3. High")
            priority_choice = input("Choose priority (1-3): ")
            priority = "Medium"
            if priority_choice == "1":
                priority = "Low"
            elif priority_choice == "3":
                priority = "High"
            add_task(title, description, priority)
        elif choice == "2":
            list_tasks()
            try:
                task_index = int(input("Enter task index to delete: "))
                delete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "3":
            list_tasks()
            try:
                task_index = int(input("Enter task index to complete: "))
                complete_task(task_index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            list_tasks()
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
