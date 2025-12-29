tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print("Task added successfully.")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
