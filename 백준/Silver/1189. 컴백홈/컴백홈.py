R, C, K = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

visited = [[False]*C for _ in range(R)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

def dfs(x, y, dist):
    global result

    if x == 0 and y == C-1:
        if dist == K:
            result += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            if not visited[nx][ny] and graph[nx][ny] == '.':
                visited[nx][ny] = True
                dfs(nx, ny, dist + 1)
                visited[nx][ny] = False 

visited[R-1][0] = True
dfs(R-1, 0, 1)

print(result)