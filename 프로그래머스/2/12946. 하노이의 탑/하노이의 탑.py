answer = []
def hanoi(n, from_, to_, mid_):
    if n == 1:
        answer.append([from_, to_])
        return
    else:
        hanoi(n-1, from_, mid_, to_)
        answer.append([from_, to_])
        hanoi(n-1, mid_, to_, from_)
        
def solution(n):
    hanoi(n, 1, 3, 2)
    return answer