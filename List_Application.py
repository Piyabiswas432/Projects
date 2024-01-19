import os

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

def mark_completed(index):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = f"[Completed] {tasks[index - 1]}"
        print("Task marked as completed.")
    else:
        print("Invalid task index.")

while True:
    print("\n==== To-Do List ====")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Delete task")
    print("4. Mark task as completed")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter the task: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Enter the task index to delete: "))
        delete_task(index)
    elif choice == "4":
        index = int(input("Enter the task index to mark as completed: "))
        mark_completed(index)
    elif choice == "5":
        print("Exiting the to-do list application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    print(tasks)