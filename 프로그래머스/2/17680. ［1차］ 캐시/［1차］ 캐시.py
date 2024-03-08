from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return 5 * len(cities)
    
    dequeue = []
    
    for city in cities:
        # print(dequeue)
        city = city.upper()
        
        isExist = False
        for i, d in enumerate(dequeue):
            if city == d:
                isExist = True
                dequeue = dequeue[:i] + dequeue[min(len(dequeue), i+1):]
                answer += 1
                break
        
        if not isExist:
            answer += 5
            if len(dequeue) == cacheSize:
                dequeue.pop(0)
                
        dequeue.append(city)
    return answer