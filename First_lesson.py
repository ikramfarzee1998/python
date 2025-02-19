import datetime

def in_task():
    input_Task = []
    while True:
        task = input("What do you plan to do: ")
    
        if task.lower() == 'stop':
            break
        input_Task.append(task)
    return input_Task
        
def write_task(input_Task):
    filename =datetime.datetime.now()
    filename =filename.strftime("%y_%b_%d")
    with open(filename+".txt", 'w') as file:
    
        print("\n planning for today: \n")
        for index, item in enumerate(input_Task, start=1):
            print(f"{index}. {item}")
            file.write(f"{index}. {item}\n")


a = in_task()
write_task(a)




