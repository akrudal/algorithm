import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i, j))

def bfs():
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>= n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1
    
bfs()
result = 0
for i in graph:
    if 0 in i:
        print(-1)
        exit()
    result = max(result,max(i))
print(result-1)