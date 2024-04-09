N, M = map(int, input().split())
castle = [[c for c in input()] for _ in range(N)]

rows = set([i for i in range(N)])
cols = set([i for i in range(M)])


temp_rows = set()
temp_cols = set()
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X':
            temp_rows.add(i)
            temp_cols.add(j)
    
rows -= temp_rows
cols -= temp_cols

print(max(len(rows), len(cols)))