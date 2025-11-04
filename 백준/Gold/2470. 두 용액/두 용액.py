import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, n - 1
best_sum = abs(arr[left] + arr[right])
ans = (arr[left], arr[right])

while left < right:
    s = arr[left] + arr[right]
    
    if abs(s) < best_sum:
        best_sum = abs(s)
        ans = (arr[left], arr[right])
    
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        break  # s == 0 → 완벽한 해
    
print(ans[0], ans[1])
