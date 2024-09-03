xs = []
ys = []
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
    
xs.sort()
ys.sort()

mid_x = xs[N//2-1 if N % 2 == 0 else N//2]
mid_y = ys[N//2-1 if N % 2 == 0 else N//2]

result = 0
for i in range(N):
    result += abs(mid_x-xs[i])
    result += abs(mid_y-ys[i])
print(result)