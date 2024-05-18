def solution(arr):
    answer = 0

    # 각 행
    for row in arr:
        answer = max(answer, sum(row))

    # 각 열
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        answer = max(answer, temp)

    # 왼쪽 대각선
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    answer = max(answer, temp)

    # 오른쪽 대각선
    temp = 0
    for i in range(100):
        temp += arr[i][99-i]
    answer = max(answer, temp)

    return answer

for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(f"#{tc} {solution(arr)}")