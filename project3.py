
#What we need to do
#User can:
#add task
#View tasks
#Delete task
#mark complete
#Loop until "exit".
#Show how many tasks completed vs pending

tasks = []

while True:
    print("\n--- TO DO MENU ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Task description: ")
        priority = input("Priority (low/med/high): ")
        tasks.append({"task": task, "priority": priority, "done": False})
        print("Task added!")

    elif choice == "2":
        for i, t in enumerate(tasks, 1):
            status = "✓" if t["done"] else "✗"
            print(f"{i}. {t['task']} ({t['priority']}) - {status}")

    elif choice == "3":
        num = int(input("Task number to complete: "))
        tasks[num-1]["done"] = True
        print("Marked as done!")

    elif choice == "4":
        num = int(input("Task number to delete: "))
        tasks.pop(num-1)
        print("Task removed!")

    elif choice == "5":
        break

# Summary
completed = sum(t["done"] for t in tasks)
pending = len(tasks) - completed

print("\n--- SUMMARY ---")
print("Completed:", completed)
print("Pending:", pending)
