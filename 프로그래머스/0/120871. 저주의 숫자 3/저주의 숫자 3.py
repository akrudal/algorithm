def solution(n):
    result = 0
    for i in range(1, n+1):
        result += 1

        while(result % 3 ==0 or '3' in str(result)):
            result += 1
            
    return result