from itertools import combinations

def solution(orders, course):
    answer = []

    orderSet = []
    combis = set()
    for order in orders:
        s = [o for o in order]
        for c in course:
            combis = combis | set(combinations(sorted(s), c))
        orderSet.append(set(s))

    combis = list(combis)
    for c in combis:
        cs = set(c)
        count = 0
        for order in orderSet:
            if len(cs) > len(order): continue
            
            if len(cs & order) == len(cs):
                count += 1

        if count >= 2:
            answer.append((''.join(sorted(c)),count))
    
    result = {}
    for a in answer:
        if len(a[0]) in result:
            print(len(a[0]), a)
            if result[len(a[0])][0][1] < a[1]:
                result[len(a[0])] = [a]
            elif result[len(a[0])][0][1] == a[1]:
                result[len(a[0])].append(a)
        else:
            result[len(a[0])] = [a]
    
    answer = []
    for key in result.keys():
        for value in result[key]:
            answer.append(value[0])
            
    return sorted(answer)