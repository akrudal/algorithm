from collections import deque

def bfs(start, target, maps):
    N, M = len(maps), len(maps[0])
    checked = [[-1] * M for i in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([start])
    checked[start[0]][start[1]] = 0
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == target:
            return checked[x][y]
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
            
            if maps[nx][ny] != 'X' and checked[nx][ny] == -1:
                queue.append((nx, ny))
                checked[nx][ny] = checked[x][y] + 1
    
    return -1


def solution(maps): 
    start = (0, 0)
    exit = (0, 0)
    lever = (0, 0)
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == "S":
                start = (i,j)
            elif maps[i][j] == "E":
                exit = (i,j)
            elif maps[i][j] == "L":
                lever = (i,j)
                
                
    count1 = bfs(start, lever, maps)
    count2 = bfs(lever, exit, maps)
    
    if count1 == -1 or count2 == -1:
        return -1
    else:
        return count1 + count2