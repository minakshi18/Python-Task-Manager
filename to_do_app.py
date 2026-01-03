def main():
    tasks = []
    
    while True:
        print("\n--- MY TO-DO LIST ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print("Task added!")
            
        elif choice == '2':
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
                
        elif choice == '3':
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
                
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()