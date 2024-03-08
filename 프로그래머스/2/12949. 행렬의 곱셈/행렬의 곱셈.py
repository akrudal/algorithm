import math

def solution(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    o = len(arr2[0])
    
    print(n, m, o)
    answer = [[0] * o for _ in range(n)]

    for i in range(n):
        for j in range(o):
            for k in range(m):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer