from collections import deque

def preprocess(n, computers):
    networks = []
    
    for i in range(n):
        temp = []
        for j in range(n):
            if i == j or computers[i][j] == 0: continue
            
            temp.append(j)
        networks.append(temp)
        
    return networks

def dfs(start, visited, networks):
    stack = [start]
    
    while stack:
        current = stack.pop()
        visited[current] = True
        
        for next in networks[current]:
            if visited[next]: continue
            stack.append(next)
    
    

def solution(n, computers):
    answer = 0
    
    networks = preprocess(n, computers)
    visited = [False] * n

    for i in range(n):
        if visited[i]: continue
        dfs(i, visited, networks)
        answer += 1
    
    return answer