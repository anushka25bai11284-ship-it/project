# Simple To-Do List App for College Project

# Store tasks in a list
tasks = []

def show_menu():
    print("\n--- College To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f" Task '{task}' added!")

def view_tasks():
    if not tasks:
        print(" No tasks yet!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f" Task '{removed}' removed!")
        except (ValueError, IndexError):
            print(" Invalid task number!")

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print(" Exiting To-Do List. Good luck with your semester!")
        break
    else:
        print(" Invalid choice, try again.")
