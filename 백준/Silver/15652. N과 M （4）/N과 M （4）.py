n, m = map(int, input().split())
selected = [0] * (m)

def recursive(x, i):
    if x == m:
        print(* selected)
    else:
        for j in range(i, n+1):
            selected[x] = j
            recursive(x+1, j)
            
recursive(0, 1)