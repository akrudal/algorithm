def solution(n):
    answers = [[0] * i for i in range(1, n+1)]

    count = 1
    for i in range(n):
        pattern = i // 3
        # 각 행의 i // 3번째 열 모음
        if i % 3 == 0:
            for answer in answers[pattern * 2: n - pattern]:
                answer[pattern] = count
                count += 1
                
        # n - i // 3번째 행 모음
        elif i % 3 == 1:
            for i in range(pattern+1, n - pattern * 2):
                answers[-1-pattern][i] = count
                count += 1
                
        #  각 행의 길이에 - i // 3 번째 열 모음
        else:
            for answer in answers[-pattern-2: -(n - pattern * 2):-1]:
                answer[-pattern-1] = count
                count += 1
    return sum(answers, [])