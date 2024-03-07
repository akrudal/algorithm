def solution(want, number, discount):
    answer = 0
    
    want_dict = { name: value for name, value in zip(want, number)}
    
    start_days = []
    for i, d in enumerate(discount):
        if not d in want: continue
        start_days.append(i)
    
    for s in start_days:
        temp = want_dict.copy()
        for i in range(s, min(s+10, len(discount))):
            if discount[i] in temp:
                temp[discount[i]] = max(temp[discount[i]] - 1, 0)
        if sum(temp.values()) <= 0 : answer += 1
        
    return answer