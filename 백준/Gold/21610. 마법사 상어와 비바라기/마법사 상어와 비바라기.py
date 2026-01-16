import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 바구니
A = [list(map(int, input().split())) for _ in range(N)]
# 이동방향
moves = [tuple(map(int, input().split())) for _ in range(M)]

# 방향: 1~8 (방향 번호 그대로 쓰기 위해 0,0)
dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 초기 구름
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for d, s in moves:
    moved = [] # 
    visited = [[False]*N for _ in range(N)]

    # 1. 구름 이동
    for r, c in clouds:
        nr = (r + dr[d]*s) % N # 경계를 초과할 경우
        nc = (c + dc[d]*s) % N
        moved.append((nr, nc))

    # 2. 비 내리기
    for r, c in moved:
        A[r][c] += 1
        visited[r][c] = True

    # 3. 구름 제거
    clouds = []

    # 4. 물복사버그
    for r, c in moved:
        cnt = 0
        for drc, dcc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            nr, nc = r + drc, c + dcc
            if 0 <= nr < N and 0 <= nc < N and A[nr][nc] > 0:
                cnt += 1
        A[r][c] += cnt

    # 5. 새 구름 생성
    for i in range(N):
        for j in range(N):
            if A[i][j] >= 2 and not visited[i][j]:
                clouds.append((i, j))
                A[i][j] -= 2

# 결과 출력
print(sum(map(sum, A)))
