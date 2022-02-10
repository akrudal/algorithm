def solution(operations):
    answer=[]
    heap=[]

    for i in operations:
        if(i[0]=="I"):
            heap.append(int(i[2:]))
        else:
            if not heap:
                continue
            heap.sort()
            if(int(i[2:])==1):
                heap.pop(-1)
            else:
                heap.pop(0)
    
    if not heap:
        answer.append(0)
        answer.append(0)
        return answer
    heap.sort()
    answer.append(heap[-1])
    answer.append(heap[0])
    return answer