n = int(input())
l = list(map(int, input().split()))
l_r = l[::-1]

dp = [1]*n
dp_r = [1]*n

for i in range(n):
    for j in range(i):
        if l[i]>l[j]:
            dp[i] = max(dp[i], dp[j]+1)
        if l_r[i]>l_r[j]:
            dp_r[i] = max(dp_r[i], dp_r[j]+1)

maximum = 0
for i in range(n):
    maximum = max(dp[i] + dp_r[n-i-1]-1, maximum)
print(maximum)