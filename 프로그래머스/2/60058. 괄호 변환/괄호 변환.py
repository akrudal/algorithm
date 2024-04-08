def isPerfect(w):
    stack = []
    for i in range(len(w)):
        if w[i] == "(":
            stack.append("(")
        else:
            if not stack: return False
            else: stack.pop()
    return True
            
def recursive(w):
    o, c = 0, 0 
    for i in range(len(w)):
        if w[i] == "(": o += 1
        else: c += 1
        
        if o == c:
            u = w[:i+1]
            v = w[i+1:]
            return u, v

def solution(p):

    if not p: return ""

    u, v = recursive(p)
    if isPerfect(u):
        return u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        for i in range(1, len(u)-1):
            if u[i] == "(":
                answer += ")"
            else:
                answer += "("

    return answer