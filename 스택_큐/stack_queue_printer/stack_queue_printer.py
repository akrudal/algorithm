import queue

def solution(priorities, location):
    answer = 0
    task_queue=queue.Queue()
    tasks=[]
    
    for i in range(len(priorities)):
        task_queue.put((priorities[i],i))
    
    while task_queue.qsize()!=0:
        check=True
        temp=task_queue.get()
        print(temp)
        for i in list(task_queue.queue):
            print(i)
            if(i[0]>temp[0]):
                check=False
                task_queue.put(temp)
                break
        if(check):
            tasks.append(temp)
    
    for i in range(len(tasks)):
        print(tasks[i][1])
        if(tasks[i][1]==location):
            answer=i
    return answer+1