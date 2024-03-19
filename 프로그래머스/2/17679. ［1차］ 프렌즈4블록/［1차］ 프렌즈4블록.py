import copy
from collections import deque

def isRemove(x, y, maps):
    dx = [1,0,1]
    dy = [0,1,1]
    
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if maps[nx][ny] != maps[x][y]:
            return False

    return True

def removeBoard(removers, board):
    total = 0
    
    dx = [0,1,0,1]
    dy = [0,0,1,1]
    
    for x,y in removers:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if board[nx][ny] == '@': 
                continue
            else:
                board[nx][ny] = '@'
                total += 1
    
    temp = copy.deepcopy(board)
    for i in range(len(temp)):
        count = 0
        for j in range(len(temp[i])):
            if temp[i][j] == '@':
                count += 1
                board[i].remove('@')
        
        for k in range(count):
            board[i].append('@')
    
    return total
        

def solution(m, n, board):
    answer = 0
    
    maps = [[0] * m for _ in range(n)]
    for j in range(n):
        for i in range(m):
            maps[j][-i-1] = board[i][j]
    
    while(True):
        removers = []
        for i in range(n-1):
            for j in range(m-1):
                if maps[i][j] == '@': break
                if isRemove(i, j, maps):
                    removers.append((i, j))
    
        if not removers:
            print(maps)
            return answer
        answer += removeBoard(removers, maps)
    
    return answer