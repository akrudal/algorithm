import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        if len(scoville) <= 0: return -1
        minimum = heapq.heappop(scoville) 
        
        if minimum >= K: return answer
    
        if len(scoville) <= 0: return -1
        minimum2 = heapq.heappop(scoville)
        
        
        heapq.heappush(scoville, minimum+minimum2*2)
        answer += 1
    
    return answer