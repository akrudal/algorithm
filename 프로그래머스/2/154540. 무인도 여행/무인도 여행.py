from collections import deque

def bfs(n, m, x, y, maps, checked):
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    
    foods = int(maps[x][y])
    checked[x][y] = True
        
    queue = deque([(x,y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue
            if maps[nx][ny] != 'X' and not checked[nx][ny]:
                checked[nx][ny] = True
                foods += int(maps[nx][ny])
                queue.append((nx, ny))
    
    return foods

def solution(maps):
    answer = []
    
    n, m = len(maps), len(maps[0])
    checked = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X' or checked[i][j]: continue
            answer.append(bfs(n, m, i, j, maps, checked))
            
    
    return sorted(answer) if answer else [-1]