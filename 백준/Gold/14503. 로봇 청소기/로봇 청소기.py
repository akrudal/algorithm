# 로봇 청소기 (BOJ 14503) — 명시적 단계 주석 포함
N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 0 = 북, 1 = 동, 2 = 남, 3 = 서
# dx, dy는 (x=r 방향, y=c 방향)로 사용
dx = [-1, 0, 1, 0]  # 북, 동, 남, 서 순서에 맞춘 x 이동
dy = [0, 1, 0, -1]

visited = [[False] * M for _ in range(N)]
x, y = r, c
result = 0

while True:
    # 1) 현재 칸이 아직 청소되지 않았으면 청소
    if not visited[x][y]:
        visited[x][y] = True
        result += 1

    # 2) 주변 4칸 중 청소되지 않은 칸이 있는지 확인하면서,
    #    반시계(왼쪽)로 한 번 회전하고 앞칸을 검사하는 동작을 최대 4번 반복
    moved = False
    for _ in range(4):
        # 반시계(왼쪽)로 회전
        d = (d + 3) % 4
        nx = x + dx[d]
        ny = y + dy[d]

        # 회전한 방향의 앞칸이 청소되지 않은 빈 칸이면 전진(한 칸 이동)하고 루프 탈출
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny
            moved = True
            break

    if moved:
        # 전진했으므로 1번으로 돌아가(while 루프 계속)
        continue

    # 3) 네 방향 모두 청소되었거나 벽인 경우 -> 후진 시도
    back_dir = (d + 2) % 4
    bx = x + dx[back_dir]
    by = y + dy[back_dir]

    # 뒤가 벽이라 후진 불가하면 종료
    if not (0 <= bx < N and 0 <= by < M) or board[bx][by] == 1:
        break
    # 후진 가능하면 한 칸 후진 (방향 d는 유지)
    x, y = bx, by

print(result)
