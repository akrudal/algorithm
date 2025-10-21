from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소한 칸 수
result = 0

# 방문 여부
visited = [[False] * M for _ in range(N)]

x, y = r, c

while True:
    # 1. 현재 칸 청소
    if not visited[x][y]:
        visited[x][y] = True
        result += 1

    cleaned = False
    for _ in range(4):
        # 2. 반시계 방향으로 회전
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 3. 앞쪽 칸이 청소되지 않은 빈 칸이라면 전진
        if board[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny
            cleaned = True
            break

    # 4. 네 방향 모두 청소가 되어 있거나 벽인 경우
    if not cleaned:
        # 뒤쪽 방향 계산
        back_dir = (d + 2) % 4
        bx = x + dx[back_dir]
        by = y + dy[back_dir]

        # 후진할 수 있다면 후진
        if board[bx][by] == 0:
            x, y = bx, by
        else:
            # 뒤가 벽이면 작동 종료
            break

print(result)
