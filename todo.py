import json
tasks=[]
def addtask(): #function to add tasks into the to-do list
    while True: 
        title=input("Enter task: ").strip()
        if not task['title'].strip(): #to prevent empty spaces as input from user
            raise ValueError("Task title cannot be empty")
        else:
            break 
        
    if len(tasks)==0: #for defining unique id's
        task_id=1
    else:
        task_id=max(task["id"] for task in tasks)+1
    

    d={'id':task_id,'title':title,'completed':False}
    tasks.append(d)
    savetasks()
    print('Task added successfully')

def savetasks(): #save tasks into the json file
    with open("tasks.json","w") as f:
        json.dump(tasks,f)

def loadtasks(): #load tasks from the json file 
    global tasks
    try:
        with open("tasks.json","r") as f:
            tasks=json.load(f)
        required_keys = ['id', 'title', 'completed']
        if not isinstance(tasks, list):
            raise ValueError("Invalid task data")

        for task in tasks: #to check the datatypes of the input stored in json 
            if not isinstance(task, dict) or not all(key in task for key in required_keys):
                raise ValueError("Invalid task structure")
            if not isinstance(task['id'], int) or isinstance(task['id'], bool):
                raise ValueError("Task ID must be an integer")
            if not isinstance(task['title'], str):
                raise ValueError("Task title must be a string")
            if not isinstance(task['completed'], bool):
                raise ValueError("Task completion status must be True or False")


    except FileNotFoundError:
        tasks=[]
        print("No task file found")
    except json.JSONDecodeError:
        tasks=[]
        print("Invalid json data")
    except ValueError as e:
        tasks = []
        print(e)

def viewtask(): 
    if len(tasks)==0:
        print("No tasks available")
        return
    print("\nYour Tasks: ")
    for task in tasks:
        print("ID:",task['id'])
        print("Title:", task["title"])
        print("Completed:", task["completed"])

def markcompleted():
    while True:
        try:
            task_id=int(input("Enter task ID to mark as completed: "))
            break
        except ValueError:
            print("Invalid Input")
    
    for task in tasks:
        if task['id']==task_id:
            task['completed']=True
            print("Task marked as completed")
            savetasks()
            return
    print("Task not found")

def removetask():
    while True:
        try:
            task_id=int(input("Enter task ID to remove: "))
            break
        except ValueError:
            print("Invalid input")
    for task in tasks:
        if task['id']==task_id:
            tasks.remove(task)
            print("Task removed successfully")
            savetasks()
            return
    print("Task not found")