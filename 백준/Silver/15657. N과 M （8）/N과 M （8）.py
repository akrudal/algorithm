n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
selected = [0] * m

def Recursive(x, i):
    if x == m:
        print(* selected)
    else:
        for (index, value) in enumerate(l):
            if index>=i:
                selected[x] = value
                Recursive(x+1, index)

Recursive(0, 0)