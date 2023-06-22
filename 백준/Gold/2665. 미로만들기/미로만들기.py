import sys
from collections import deque

# input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(x,y):
    queue = deque([(x,y,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    visited = [[0]*(n) for _ in range(n)]
    
    while queue:
        x,y,count = queue.popleft()
        if x == n-1 and y == n-1:
            print(count)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <0 or nx >= n or ny < 0 or ny >= n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if graph[nx][ny] == 0:
                    queue.append((nx,ny,count+1))
                else:
                    queue.appendleft((nx,ny,count))

bfs(0,0)