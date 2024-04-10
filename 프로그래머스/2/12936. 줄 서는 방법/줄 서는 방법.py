from itertools import permutations

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def solution(n, k):
    answer = []
    
    k -= 1
    li = [i for i in range(1,n+1)]
    
    while len(answer) < n:
        maxK = factorial(len(li))
        count = maxK // len(li)
        num = li[(k//count)]

        li.remove(num)
        answer.append(num)
        
        k %= count
    
    return answer