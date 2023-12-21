import os

def display_menu():
    print("Todo List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def view_tasks():
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
        if tasks:
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task.strip()}")
        else:
            print("No tasks found.")

def add_task():
    task = input("Enter task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully.")

def mark_task_done():
    view_tasks()
    task_index = int(input("Enter the task number to mark as done: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1] = "[Done] " + tasks[task_index - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task marked as done.")
    else:
        print("Invalid task number.")

def delete_task():
    view_tasks()
    task_index = int(input("Enter the task number to delete: "))
    with open("tasks.txt", "r") as file:
        tasks = file.readlines()
    if 1 <= task_index <= len(tasks):
        del tasks[task_index - 1]
        with open("tasks.txt", "w") as file:
            file.writelines(tasks)
        print("Task deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    if not os.path.exists("tasks.txt"):
        with open("tasks.txt", "w"):
            pass

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the Todo List. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
