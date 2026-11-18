from task_manager import TaskManager


def show_menu():
    print("\n=== Student Task Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")


def handle_add(manager):
    title = input("Task title: ")
    manager.add_task(title)
    print("Task added.")


def handle_view(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        status = "x" if t["completed"] else " "
        print(f"[{status}] {t['id']}. {t['title']}")


def handle_complete(manager):
    print("Not implemented yet.")


def handle_delete(manager):
    raw_id = input("Enter task ID to delete: ").strip()
    if not raw_id.isdigit():
        print("Error: Please enter a valid number.")
        return
    try:
        task = manager.delete_task(int(raw_id))
        print(f"Task '{task['title']}' deleted.")
    except ValueError as error:
        print(f"Error: {error}")


def main():
    manager = TaskManager()
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            handle_add(manager)
        elif choice == "2":
            handle_view(manager)
        elif choice == "3":
            handle_complete(manager)
        elif choice == "4":
            handle_delete(manager)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()