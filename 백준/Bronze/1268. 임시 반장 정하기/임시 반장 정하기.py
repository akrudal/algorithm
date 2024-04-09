N = int(input()) # 3 이상 1000 이이상
table = [[int(c) for c in input().split()] for _ in range(N)]

result = (0, 0) # 몇 번 학생, 몇 명
for i in range(N):
    count = set()
    for j in range(5):
        for k in range(N):
            if i == k: continue
            if table[i][j] == table[k][j]:
                count.add(k)
    
    if result[1] < len(count):
        result = (i, len(count))


print(result[0] + 1)