# 도시의 N개의 빌딩
N = int(input())
numbers = [int(input()) for _ in range(N)]
stack = []

buildingSum = 0

for n in numbers:
    while stack and stack[-1] <= n:
        stack.pop()
    stack.append(n)
    buildingSum += len(stack) - 1

print(buildingSum)
