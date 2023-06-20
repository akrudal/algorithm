import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
hx,hy = map(int, input().split())
ex,ey = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs(x,y,ex,ey):
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    queue = deque([(x,y,0)])
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    while queue:
        x,y,z = queue.popleft()
        if x== ex and y==ey:
            print(visited[x][y][z])
            return
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if nx < 0 or nx >= n or ny <0 or ny>=m:
                continue
            
            if z == 0:
                if graph[nx][ny] == 0 and visited[nx][ny][0] == 0:
                    queue.append((nx,ny,0))
                    visited[nx][ny][0] = visited[x][y][0] + 1
                elif graph[nx][ny] == 1 and visited[nx][ny][1] == 0:
                    queue.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][0] + 1
            else:
                if graph[nx][ny] == 0 and visited[nx][ny][1] == 0:
                    queue.append((nx,ny,1))
                    visited[nx][ny][1] = visited[x][y][1] + 1
    print(-1)
                    
bfs(hx-1,hy-1,ex-1,ey-1)