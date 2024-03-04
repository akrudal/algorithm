def solution(ss):
    
    if len(ss) % 2 != 0: return 0
    stack = []
    
    for s in ss:
        if not stack or stack[-1] != s:
            stack.append(s)
        else:
            stack.pop()
    return 0 if stack else 1

print(solution('baabaa'))