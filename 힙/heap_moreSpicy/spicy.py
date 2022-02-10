import heapq

def solution(scoville, K):
    answer = 0
    heap=[]
    
    for i in scoville:
        heapq.heappush(heap,i)
    
    while len(heap)!=1:
        if(heap[0]>=K):
            break
        nSpicy1=heapq.heappop(heap)
        nSpicy2=heapq.heappop(heap)
        
        mix=nSpicy1+nSpicy2*2
        heapq.heappush(heap,mix)
        
        answer+=1

    if(heap[0]<K):
        answer=-1
    return answer