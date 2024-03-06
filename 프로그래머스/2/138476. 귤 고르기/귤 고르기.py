def solution(k, tangerine):
    d = {}
    for t in tangerine:
        if t in d:
            d[t] += 1
        else:
            d[t] = 1
    
    tangerine = sorted(d.items(), key = lambda item: -item[1])
    answer = 0
    
    for (size, count) in tangerine:
        if k <= 0: break
        
        k -= count
        answer += 1
    
    
    return answer