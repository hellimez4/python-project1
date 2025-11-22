# 3. To-Do List App (Text-Based)
# Build a to-do list manager that:
# Allows users to add tasks with priorities (e.g., "Buy milk - high").
# Lets them view the current list,  delete tasks by number, and  mark tasks as complete.
# Keeps looping until the user types “Exit”.
# Shows a summary at the end: number of completed tasks vs pending.
# Skills practiced: lists, string parsing, loops, input, CRUD basics.



def summury():
    completed = sum(t["status"] == "completed" for t in tasks)
    pending = sum(t["status"] == "pending" for t in tasks)

    print("\n----- SUMMARY -----")
    print(f"Completed: {completed}")
    print(f"Pending:   {pending}\n")

    print("Your To-Do List:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['name']} — {t['Periority']} — {t['status']}")
    


tasks=[]   
Periorities={1:'high',2:'medium', 3:'low'}


while True:
    req=input('enter task or Exit: ').strip().lower()
    if  req =='exit':
        print(summury())
        break

    elif req.isalpha() == False:
        print('task must be in letter')
        continue

    print('Choose periority:')
    for k, v in Periorities.items():
     print(f"{k}. {v}")

    p=input('enter perioritties: ').strip()
    if not p.isnumeric() or int(p) not in Periorities:
        print('invalid!  please enter right periority number')
        continue

#Task
    task={'name':req, 'Periority':Periorities[int(p)],'status':'pending'}

    tasks.append(task)
    print(f"task you added {task}")

#Modification
    modify=input('do you want to modift?  yes or no?:  ').strip().lower()

    if modify== 'yes':

        action=input('do you want to delete? or modifiy? write either delete or modifiy: ').strip().lower()
        if action =='delete':
            index=input('if you want to delete inter number of task: ').strip()
            if index.isnumeric()==False:
                print('invalide number')
                continue
            else:
              del tasks[int(index)]
              print('task deleted')
        elif action=='complete':
              task['status']='Complete'
              print('task marked as complete')
    continue          
        


