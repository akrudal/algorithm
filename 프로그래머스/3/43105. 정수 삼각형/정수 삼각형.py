def solution(triangle):
    length = len(triangle)
    
    dp = [[0] * (i+1) for i in range(length)]
    dp[0][0] = triangle[0][0]
    
    for i in range(1, length):
        for j in range(len(triangle[i-1])):
            
            if dp[i][j] == 0:
                dp[i][j] = triangle[i][j]
            if dp[i][j+1] == 0:
                dp[i][j+1] = triangle[i][j+1]
                
            dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i-1][j])
            dp[i][j+1] = max(dp[i][j+1], triangle[i][j+1] + dp[i-1][j])
            

        
    return max(dp[-1])