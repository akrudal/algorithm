def solution(targets):
    targets.sort(key=lambda x: x[1])

    answer = 0
    last = -1

    for s, e in targets:
        if last <= s:
            answer += 1
            last = e

    return answer