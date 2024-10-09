def solution(m, n, puddles):
    puddles_set = set((y-1, x-1) for x, y in puddles)
    
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            if (i, j) in puddles_set:
                dp[i][j] = 0
            else:
                if i > 0: 
                    dp[i][j] += dp[i-1][j]
                if j > 0: 
                    dp[i][j] += dp[i][j-1]
    
    return dp[n-1][m-1] % 1000000007