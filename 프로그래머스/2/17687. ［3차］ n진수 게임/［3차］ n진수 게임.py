# 진법 n, 숫자 m
def convert(n, m):
    result = ""
    while(m > 0):
        temp = m % n
        result += str(temp) if temp < 10 else chr(temp - 10 + 65)
        m = m // n
    
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    
    stack = "0"
    num = 1
    while(len(stack) < t*(m+1)):
        stack += convert(n, num)
        num += 1
    
    count = t
    for i in range(0, t*(m+1) ,m):
        if count == 0 : break
        answer += stack[i+p-1]
        count -= 1
    return answer