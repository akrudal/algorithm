def solution(k, d):
    answer = 0
    
    for x in range(0,d+1,k):
        y = ((d ** 2 - x ** 2)**(1/2))
        answer += y // k
    answer += d // k + 1
    return answer