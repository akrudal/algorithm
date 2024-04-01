def solution(storey):
    ss = str(storey)
    answer = int(ss[0])
    
    for s in ss[1:]:
        i = int(s)
        if i >= 5:
            answer += (10 - i) + 1
        else:
            answer += i
    
    temp = int(ss[0])
    for s in ss[1:]:
        i = int(s)
        if i > 5:
            temp += (10 - i) + 1
        else:
            temp += i
    
    answer = min(answer, temp)
    
    r_ss = ss[::-1]
    temp = 0
    isUp = False
    for s in r_ss:
        i = int(s) + 1 if isUp else int(s)
        if i > 5:
            temp += 10 - i
            isUp = True
        else:
            temp += i
            isUp = False
    if isUp: temp += 1
    answer = min(answer, temp)
    
    temp = 0
    isUp = False
    for s in r_ss:
        i = int(s) + 1 if isUp else int(s)
        if i >= 5:
            temp += 10 - i
            isUp = True
        else:
            temp += i
            isUp = False
    if isUp: temp += 1
    
    print(temp)
    return min(answer,temp)