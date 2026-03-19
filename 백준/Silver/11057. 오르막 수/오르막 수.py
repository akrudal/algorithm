N = int(input())
MOD = 10007

dp = [1]*10  # 길이 1

for _ in range(2, N+1):
    for j in range(1, 10):
        dp[j] = (dp[j] + dp[j-1]) % MOD

print(sum(dp) % MOD)