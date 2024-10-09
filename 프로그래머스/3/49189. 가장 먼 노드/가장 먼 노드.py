from collections import deque

def dfs(n, graphs):
    answer = [0] * (n+1)
    
    queue = deque([1])
    visited = [False] * (n+1)
    visited[1] = True
    
    while queue:
        current_node = queue.popleft()
        next_nodes = graphs[current_node]
        
        for next_node in next_nodes:
            if not visited[next_node]:
                visited[next_node] = True
                answer[next_node] = answer[current_node] + 1
                queue.append(next_node)
    
    return answer.count(max(answer))
    

def solution(n, edge):
    graphs = {}
    for (x,y) in edge:
        if x in graphs:
            graphs[x].append(y)
        else:
            graphs[x] = [y]
            
        if y in graphs:
            graphs[y].append(x)
        else:
            graphs[y] = [x]
    
    return dfs(n, graphs)