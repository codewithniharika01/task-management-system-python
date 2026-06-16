def task():
    tasks = []

    print("----------WELCOME TO THE TASK MANAGEMENT----------")

    total_task = int(input("Enter how many tasks you want to add = "))

    for i in range(1, total_task + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)

    print(f"Today's tasks are:\n{tasks}")

    while True:
        operation = int(input(
            "\nEnter:\n"
            "1 - Add Task\n"
            "2 - Update Task\n"
            "3 - Delete Task\n"
            "4 - View Tasks\n"
            "5 - Exit\n"
            "Choice = "
        ))

        if operation == 1:
            add = input("Enter task name to add = ")
            tasks.append(add)
            print(f"Task '{add}' has been added successfully.")

        elif operation == 2:
            updated_val = input("Enter task name to update = ")

            if updated_val in tasks:
                up = input("Enter new task name = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task updated to '{up}'.")
            else:
                print("Task not found.")

        elif operation == 3:
            del_val = input("Enter task name to delete = ")

            if del_val in tasks:
                tasks.remove(del_val)
                print(f"Task '{del_val}' deleted successfully.")
            else:
                print("Task not found.")

        elif operation == 4:
            print("\nCurrent Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t}")

        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice. Please try again.")

    print("Thank You!")


task()