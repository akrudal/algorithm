from collections import deque

def search(lands):
    dp = [[0] * 4 for i in range(len(lands))]
    dp[0] = lands[0]
    
    for i in range(1, len(lands)):
        for j in range(4):
            maximum = 0
            for k in range(4):
                if j == k: continue
                maximum = max(maximum, dp[i-1][k])
            dp[i][j] = maximum + lands[i][j]
    return max(dp[-1])

def solution(lands):
    return search(lands)