def solution(x, y, n):
    dp = [-1] * (y+1)
    dp[x] = 0
    for i in range(x, y):
        count = dp[i]
        if count == -1: continue
        
        temp = i * 3
        if temp <= y:
            if dp[temp] == -1:
                dp[temp] = count + 1
            else:
                dp[temp] = min(dp[temp], count+1)
            
        temp = i * 2
        if temp <= y:
            if dp[temp] == -1:
                dp[temp] = count + 1
            else:
                dp[temp] = min(dp[temp], count+1)
        
        temp = i+n
        if temp <= y:
            if dp[temp] == -1:
                dp[temp] = count + 1
            else:
                dp[temp] = min(dp[temp], count+1)
    return dp[y]