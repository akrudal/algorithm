import sys
input = sys.stdin.readline

n = int(input())

# 이동횟수는 2^n - 1
# 가장 큰 원판을 옮기려면 어떻게 해야하지? start 1에서 나머지가 temp에 n번째가 마지막에 존재해야함
# 그러면 n-1번째를 모두 temp로 옮겨야함 temp ->가 end에 위치하게 되는 것
print((1 << n) - 1)   

def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    
    hanoi(n-1, start, temp, end)
    print(start, end)
    hanoi(n-1, temp, end, start)

if n <= 20:
    hanoi(n, 1, 3, 2)