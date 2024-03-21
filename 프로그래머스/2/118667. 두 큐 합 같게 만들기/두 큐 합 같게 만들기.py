def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1+sum2) / 2
    if (sum1+sum2) % 2 !=0: return -1
    # print("target:", target, "sum1:", sum1, "sum2:", sum2)

    length = len(queue1)
    answer = 0
    index1 = 0
    index2 = 0
    for i in range(length * 3 ):
        if sum1 == sum2:
            return answer
        
        if sum1 > target:
            temp = queue2[index1-length] if index1 >= length else queue1[index1]
            index1 += 1
            sum1 -= temp
            sum2 += temp
        
        elif sum2 > target:
            temp = queue1[index2-length] if index2 >= length else queue2[index2]
            index2 += 1
            sum2 -= temp
            sum1 += temp
        
        answer += 1
    
    return -1