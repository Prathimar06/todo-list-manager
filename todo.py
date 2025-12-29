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
    print("3. Delete Task")
    print("4.exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        show_tasks()
        num = int(input("Enter task number to delete: "))
        delete_task(num)
    elif choice == "4":
        print("Goodbye!")
        break

def delete_task(index):
    try:
        removed = tasks.pop(index - 1)
        print(f"Removed task: {removed}")
    except IndexError:
        print("Invalid task number.")
