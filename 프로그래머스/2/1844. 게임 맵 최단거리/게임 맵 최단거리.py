from collections import deque

def dfs(n, m, maps):
    checked = [[0] * m for _ in range(n)]
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    
    que = deque([(0,0)])
    checked[0][0] = 1
    
    while que:
        x, y = que.popleft()
        if x == n -1 and y == m -1:
            return checked[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx >= n or nx <0 or ny< 0 or ny >= m: continue
            if checked[nx][ny] != 0 or maps[nx][ny] == 0: continue
            
            checked[nx][ny] = checked[x][y] + 1
            que.append((nx, ny))
    
    return -1

def solution(maps):
    answer = 0
    
    return dfs(len(maps), len(maps[0]), maps)