H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 왼쪽 최대 높이
left_max = [0] * W
left_max[0] = blocks[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], blocks[i])

# 오른쪽 최대 높이
right_max = [0] * W
right_max[W - 1] = blocks[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], blocks[i])

# 빗물 계산
answer = 0
for i in range(W):
    water = min(left_max[i], right_max[i]) - blocks[i]
    if water > 0:
        answer += water

print(answer)
