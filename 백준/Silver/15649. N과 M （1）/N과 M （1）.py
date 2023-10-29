import sys
sys.setrecursionlimit(10**6)

a, b = map(int, input().split())

lst = [ (i+1) for i in range(a)]
checked = [False for i in range(a+1)]
selected = [0] * b

def Recur(n):
    if n == b:
        print(*selected)
    else:
        for i in range(1,a+1):
            if checked[i]:
                continue
            else:
                selected[n]= i
                checked[i] = True
                Recur(n+1)
                checked[i] = False
                
Recur(0)