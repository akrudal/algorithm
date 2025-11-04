# 입력받기
A = input().strip()
B = input().strip()

lenA, lenB = len(A), len(B)

# DP 테이블 생성 (모두 0으로 초기화)
dp = [[0] * (lenB + 1) for _ in range(lenA + 1)]

# 테이블 채우기
for i in range(1, lenA + 1):
    for j in range(1, lenB + 1):
        if A[i - 1] == B[j - 1]:     # 문자가 같을 때
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:                         # 문자가 다를 때
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 결과 출력
print(dp[lenA][lenB])
