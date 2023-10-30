n, m = map(int, input().split())
# checked = [False] * (n+1)
selected = [0] * (m)

def recursive(x):
    if x == m:
        print(* selected)
    else:
        for i in range(1, n+1):
            # if not checked[i]:
            selected[x] = i
                # checked[i] = True  
            recursive(x+1)
                # checked[i] = False
            
recursive(0)