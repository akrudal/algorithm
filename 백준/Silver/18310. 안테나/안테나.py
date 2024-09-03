N = int(input())
houses = sorted(list(map(int, input().split())))
if N % 2 == 0:
    print(houses[N//2-1])
else:
    print(houses[N//2])