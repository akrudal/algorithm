def solution(babbling):
    answer = 0
    can = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        l = len(b)
        for c in can:
            l -= b.count(c) * len(c)
        if l == 0: answer += 1
    return answer