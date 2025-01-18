def main():
    tasks = []

    while True:
        print("\n ---TO DO LIST--- ")
        print("1.Add Task")
        print("2.Show Tasks")
        print("3.Mark Task has Done")
        print("4.Exit")
        choice = input("Enter Your Choice:")
        if choice =='1':
            print()
            n_tasks = int(input("How Many Tasks You want To Add"))
            for i in range(n_tasks):
                task = input("Enter The Task:")
                tasks.append({"task": task, "done": False})
                print("Task added!")
        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(tasks):
                status = "Done" if task["done"] else "Not Done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice =='3':
            task_index = int(input("Enter the Task number to mark as done")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Tasks marked as done!")
            else:
                print("Invalid Task number") 
        else:
            print("Invalid Choice.Please try Again")
if __name__ == "__main__":
    main()         


