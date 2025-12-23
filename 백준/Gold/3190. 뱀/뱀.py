from collections import deque

N = int(input())
K = int(input())

apples = set()
for _ in range(K):
    r, c = map(int, input().split())
    apples.add((r-1, c-1))

L = int(input())
turns = deque()
for _ in range(L):
    X, C = input().split()
    turns.append((int(X), C))

# 방향: 오른쪽, 아래, 왼쪽, 위
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = deque()
snake.append((0, 0))
snake_set = {(0, 0)}

direction = 0
time = 0

while True:
    time += 1
    head_x, head_y = snake[0]
    nx = head_x + dx[direction]
    ny = head_y + dy[direction]

    # 벽 충돌
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        break

    # 자기 몸 충돌
    if (nx, ny) in snake_set:
        break

    # 머리 이동
    snake.appendleft((nx, ny))
    snake_set.add((nx, ny))

    # 사과 처리
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        tail = snake.pop()
        snake_set.remove(tail)

    # 방향 전환
    if turns and time == turns[0][0]:
        _, C = turns.popleft()
        if C == 'L':
            direction = (direction + 3) % 4
        else:  # 'D'
            direction = (direction + 1) % 4

print(time)
