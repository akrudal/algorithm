import sys
input = sys.stdin.readline

N = 19
board = [list(map(int, input().split())) for _ in range(N)]

# 4방향: →, ↓, ↘, ↗
dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]

for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            continue

        color = board[r][c]

        for dr, dc in dirs:
            # 시작 이전 칸 검사
            pr, pc = r - dr, c - dc
            if 0 <= pr < N and 0 <= pc < N and board[pr][pc] == color:
                continue

            cnt = 1
            nr, nc = r + dr, c + dc

            # 같은 색 연속 세기
            while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color:
                cnt += 1
                nr += dr
                nc += dc

            # 정확히 5개인지 확인
            if cnt == 5:
                # 뒤 칸 검사 (6목 이상 차단)
                if 0 <= nr < N and 0 <= nc < N and board[nr][nc] == color:
                    continue

                print(color)
                print(r + 1, c + 1)
                sys.exit()

print(0)
