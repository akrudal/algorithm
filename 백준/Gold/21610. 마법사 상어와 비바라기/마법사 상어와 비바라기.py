import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
moves = [tuple(map(int, input().split())) for _ in range(M)]

# 방향 (1~8)
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# visited를 턴 번호로 재사용
visited = [[0]*N for _ in range(N)]
turn = 1

for d, s in moves:
    new_clouds = []

    # 1. 구름 이동 + 2. 비 내리기
    for r, c in clouds:
        nr = (r + dr[d]*s) % N
        nc = (c + dc[d]*s) % N
        A[nr][nc] += 1
        visited[nr][nc] = turn
        new_clouds.append((nr, nc))

    # 3. 구름 사라짐
    clouds = []

    # 4. 물복사버그
    for r, c in new_clouds:
        cnt = 0
        for drc, dcc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            nr, nc = r + drc, c + dcc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                cnt += 1
        A[r][c] += cnt

    # 5. 새 구름 생성
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and visited[i][j] != turn:
                clouds.append((i, j))
                A[i][j] -= 2

    turn += 1

# 결과
print(sum(map(sum, A)))
