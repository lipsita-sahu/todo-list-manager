import todo

todo.loadtasks()

while True:  #menu driven program 
    print("\nWelcome to the To-Do List Manager!")
    print("1.Add Task\n2.View Task\n3.Mark Completed\n4.Remove Task")
    try:
        n=int(input("Enter the task to be done: "))
    except ValueError:
        print("Please enter a number")
        continue

    if n==1:
        todo.addtask()
    elif n==2:
        todo.viewtask()
    elif n==3:
        todo.markcompleted()
    elif n==4:
        todo.removetask()
    elif n<1 or n>5:
        print("Invalid Choice, choose another number")
        break