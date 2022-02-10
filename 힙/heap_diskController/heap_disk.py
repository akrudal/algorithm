import math

def solution(jobs):
    answer = 0
    index=0
    heap=[]
    
    jobs.sort(key=lambda x: (x[0], x[1]))
    time=jobs[0][0]
    
    while True:
        if(index>=len(jobs) and not heap):
            break
        for j in range(index,len(jobs)):
            if(time<jobs[j][0]):
                break
            else:
                index=j+1
                heap.append(jobs[j])
        if(index<len(jobs) and not heap):
            heap.append(jobs[index])
            time=jobs[index][0]
            index+=1
            continue
            
        heap.sort(key=lambda x:x[1])
        
        answer+=(time+heap[0][1]-heap[0][0])
        time+=heap[0][1]
        heap.pop(0)

        
    answer/=len(jobs)
    return math.trunc(answer)