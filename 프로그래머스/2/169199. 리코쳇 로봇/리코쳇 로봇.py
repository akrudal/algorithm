from collections import deque

def bfs(board, x, y):
    N, M = len(board), len(board[0])
    checked = [[False]*M for _ in range(N)]
    queue = deque([(x,y,0)])
    
    while queue:
        x, y, z = queue.popleft()
        
        if x<0 or x>=N or y<0 or y>=M or checked[x][y]: continue
        if board[x][y] == 'G':
            return z
        
        up, down, left, right = -1, 1, -1, 1
        while(0<=x+up<N and board[x+up][y] != 'D'):
            up -= 1
        queue.append((x+up+1, y, z+1))
        
        while(0<=x+down<N and board[x+down][y] != 'D'):
            down += 1
        queue.append((x+down-1, y, z+1))
        
        while(0<=y+left<M and board[x][y+left] != 'D'):
            left -= 1
        queue.append((x, y+left+1, z+1))
        
        while(0<=y+right<M and board[x][y+right] != 'D'):
            right += 1
        queue.append((x, y+right-1, z+1))
    
        checked[x][y] = True
    return -1
    

def solution(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                return bfs(board, i, j)