n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
checked = [False for _ in range(n)]
result = [0 for _ in range(m)]

def recursive(x):
    if x == m:
        print(*result)
        return
    else:
        for i in range(n):
            if not checked[i]:
                checked[i] = True
                result[x] = n_list[i]
                recursive(x+1)
                checked[i] = False

recursive(0)