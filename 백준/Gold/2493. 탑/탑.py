N = int(input())
tops = list(map(int, input().split()))

stack = []
answer = [0] * N

for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, tops[i]])

print(*answer)