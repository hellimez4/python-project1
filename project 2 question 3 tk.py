# Function Definition: Defines the main block of code that runs
def to_do_list(): 
    # 1. We'll be using a List to store multiple Dictionaries (for task storage).
    tasks = [] 
    
    # 2. while True loop: Keeps the todo menu running until the user types 'exit'.
    while True: 
        
        # Display the main menu options using 'print' and 'strings'
        print("\n===== To-Do List =====") 
        print("1. Add Task (with priority)") # Allows users to add tasks with priorities (e.g., "Buy milk - high").
        print("2. Show Tasks") # View the current list.
        print("3. Mark Task as Done") # Mark tasks as complete.
        print("4. Delete Task") # Delete tasks by number.
        print("5. Exit") # Closing the loop.
        
        # user enters their choice as "input"
        choice = input("Enter your choice (1-5): ") # choice variable
        
        # --- A. ADD TASK (Create) ---
        if choice == '1': # 'if' is a conditional statement (Control Flow Structure)
            # Get user input for task and priority (e.g., "Buy milk-high")
            # MAKE SURE TO ENTER WITH HYPHEN NO SPACE 
            task_input = input("Enter task and priority (e.g., 'Task Name-high'): ")
            
            parts = task_input.split('-', 1) # String Parsing: Split the input by the hyphen '-'
            task_name = parts[0].strip() # Get the task name
            # Get priority or default to 'medium' if none is provided
            priority = parts[1].strip().lower() if len(parts) > 1 else 'medium'
            
            # Add the new task dictionary to the 'tasks' list
            tasks.append({
                "task": task_name,
                "priority": priority,
                "done": False # All new tasks start as not done (Boolean)
            })
            print(f"Task '{task_name}' added with priority: {priority.upper()}")

        # --- B. SHOW TASKS (Read) ---
        elif choice == '2':
            if not tasks: # Check if the list is empty (Boolean check)
                print("Your To-Do List is empty!")
                continue # Go back to the start of the loop
            
            print("\n----- Current To-Do List -----")
            # Loop through the list, assigning an 'index' for numbering
            for index, task in enumerate(tasks):
                # Use a conditional expression to set the display status
                status = "✔️ Done" if task["done"] else "❌ Pending"
                
                # Print the task number (index + 1), name, priority, and status
                print(f"{index + 1}. {task['task']} ({task['priority'].upper()}) - {status}")
            print("------------------------------")

        # --- C. MARK AS DONE (Update) ---
        elif choice == '3':
            # Ask which task number to mark done
            try:
                task_num = int(input("Enter the number of the task to mark as done: "))
                # Convert the user-friendly number to the zero-based list index
                task_index = task_num - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            # Check if the index is valid (within the list range)
            if 0 <= task_index < len(tasks):
                # Update the 'done' key for the specific task to True
                tasks[task_index]["done"] = True
                print(f"Task {task_num} marked as done!")
            else:
                print("Invalid task number.")

        # --- D. DELETE TASK (Delete) ---
        elif choice == '4':
            # Ask which task number to delete
            try:
                task_num = int(input("Enter the number of the task to delete: "))
                task_index = task_num - 1
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            
            # Check if the index is valid
            if 0 <= task_index < len(tasks):
                # Remove the task from the list using the .pop() method
                deleted_task = tasks.pop(task_index)
                print(f"Task '{deleted_task['task']}' deleted.")
            else:
                print("Invalid task number.")

        # --- E. EXIT and SUMMARY ---
        elif choice == '5' or choice.lower() == 'exit':
            print("Exiting the To-Do List manager...")
            break # Exit the while loop
        
        # --- F. INVALID CHOICE ---
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
    
    # --- 3. FINAL SUMMARY: Runs only AFTER the loop is exited ---
    completed_count = 0
    pending_count = 0
    
    # Loop through the final list to count statuses
    for task in tasks:
        if task['done']:
            completed_count += 1
        else:
            pending_count += 1
    
    # Print the final report
    print("\n===== FINAL REPORT =====")
    print(f"Completed Tasks: {completed_count}")
    print(f"Pending Tasks:   {pending_count}")
    print(f"Total Tasks:     {len(tasks)}")
    print("========================\nThank you for using the To-Do Manager!")

# This line ensures the 'to_do_list' function is run when the script starts
if __name__ == "__main__":
    to_do_list()