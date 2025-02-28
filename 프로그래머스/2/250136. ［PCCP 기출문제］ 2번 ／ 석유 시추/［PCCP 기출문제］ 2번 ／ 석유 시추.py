from collections import deque

def solution(land):
    answer = 0
    n = len(land)
    m = len(land[0])
    checked = [[-1] * m for _ in range(n)]

    index = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and checked[i][j] == -1:
                bfs(land, i, j, checked, index)
                index+=1
                
    for j in range(m):
        temp = 0
        p_set = set()
        for i in range(n):
            if land[i][j] != 0 and (not checked[i][j] in p_set):
                temp += land[i][j]
                p_set.add(checked[i][j])
        answer = max(temp, answer)
    
    return answer
    
def bfs(land, x, y, checked, index):
    n = len(land)
    m = len(land[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    petroleumns = [(x, y)]
    queue = deque([(x,y)])
    checked[x][y] = index
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x+ dx[i]
            ny = y+ dy[i]
            
            if nx<0 or nx>=n or ny<0 or ny>=m or checked[nx][ny] != -1: continue
            if land[nx][ny] == 1:
                petroleumns.append((nx,ny))
                checked[nx][ny] = index
                queue.append((nx,ny))
    
    count = len(petroleumns)
    for x,y in petroleumns:
        land[x][y] = count
    
                
    
        