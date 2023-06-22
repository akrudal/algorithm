n = int(input())
l = list(map(int, input().split()))

dp = [1]*n
dp_r = [1]*n

for i in range(1,n):
    if l[i] >= l[i-1]:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = 1

    if l[-i] <= l[-i-1]:
        dp_r[i] = dp_r[i-1]+1
    else:
        dp_r[i] = 1

x = max(dp)
y = max(dp_r)
print(max(x,y))