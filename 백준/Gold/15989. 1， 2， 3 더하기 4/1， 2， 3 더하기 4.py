T = int(input())
nums = [int(input()) for _ in range(T)]

m = max(nums)

dp = [0]*(m+1)
dp[0] = 1

for num in [1,2,3]:
    for i in range(num, m+1):
        dp[i] += dp[i-num]

for n in nums:
    print(dp[n])