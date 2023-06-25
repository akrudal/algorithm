from collections import deque

n, k = map(int, input().split())

def bfs(x):
    visited = [0]*(100001)
    queue = deque([x])
    visited[x] = 1
    
    while queue:
        x = queue.popleft()
        
        if x == k:
            return visited[x]-1
        if 0<=2*x<100001 and visited[2*x] == 0:
            visited[2*x] = visited[x]
            queue.append(2*x)
        if 0<=x-1<100001 and visited[x-1] == 0:
            visited[x-1] = visited[x] + 1
            queue.append(x-1)
        if 0<=x+1<100001 and visited[x+1] == 0:
            visited[x+1] = visited[x] + 1
            queue.append(x+1)
print(bfs(n))