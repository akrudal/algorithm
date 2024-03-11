def makeDict():
    d = {}
    
    i = 1
    for s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        d[s] = i
        i += 1
    return d

def solution(msg):
    answer = []
    
    num = 27
    dic = makeDict()
    
    maximum = 1
    i = 0
    while(i <= len(msg) -1):
        temp_i = i
        temp = dic[msg[i]]
        
        for j in range(i + 1, i + maximum + 2):
            check_str = msg[i:j]
            if check_str in dic: 
                temp = dic[check_str]
                temp_i = j
            else:
                dic[check_str] = num
                maximum = max(maximum, len(check_str))
                num += 1
                break
        i = temp_i
        answer.append(temp)
    
    return answer