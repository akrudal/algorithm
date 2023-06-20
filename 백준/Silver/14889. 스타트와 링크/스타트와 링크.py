import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def get_combinations(arr,n):
    result = []
    if n == 0:
        return [[]]
    
    for i in range(0, len(arr)):
        elem = arr[i]
        rest_arr = arr[i+1:]
        for c in get_combinations(rest_arr, n-1):
            result.append([elem]+c)
    return result

temp = [i for i in range(1,n+1)]
combinations = get_combinations(temp, n/2)
minimum = 999999

for i in range(len(combinations)//2):
    left = 0
    for j in combinations[i]:
        for k in combinations[i]:
            if j!= k:
                left+=arr[j-1][k-1]    
    right = 0
    for j in combinations[-i-1]:
        for k in combinations[-i-1]:
            if j!= k:
                right += arr[j-1][k-1]
    
    minimum = min(minimum, abs(left-right))
print(minimum)