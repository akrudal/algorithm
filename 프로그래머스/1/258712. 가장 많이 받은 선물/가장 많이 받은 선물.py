def solution(friends, gifts):
    answer = 0
    
    n = len(friends)
    friend_dict = {}
    record_dict = {}
    point_dict = {}
    result = [0] * n
    
    for i,friend in enumerate(friends):
        friend_dict[friend] = i
        record_dict[friend] = [0]*n
        # 준 선물, 받은 선물
        point_dict[friend] = [0, 0]
    
    for gift in gifts:
        fromm, to = gift.split()
        record_dict[fromm][friend_dict[to]] += 1
        point_dict[fromm][0] += 1
        point_dict[to][1] += 1
        
    for i in range(n):
        for j in range(i, n):
            fromm = friends[i]
            to = friends[j]
            
            fromto = 0
            tofrom = 0
            # 두 사람이 선물을 주고받은 기록이 있다면
            fromto = record_dict[fromm][friend_dict[to]]
            tofrom = record_dict[to][friend_dict[fromm]]
            
            if fromto == tofrom:
                #선물지수
                fromPoint = point_dict[fromm][0] - point_dict[fromm][1]
                toPoint = point_dict[to][0] - point_dict[to][1]
                
                if fromPoint < toPoint:
                    result[friend_dict[to]] += 1
                elif fromPoint > toPoint:
                    result[friend_dict[fromm]] += 1
            else:
                if fromto > tofrom:
                    result[friend_dict[fromm]] += 1
                elif fromto < tofrom:
                    result[friend_dict[to]] += 1

    return max(result)