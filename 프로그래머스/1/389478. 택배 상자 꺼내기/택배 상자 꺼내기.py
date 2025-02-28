def solution(n, w, num):
    answer = n // w
    index = 0
    current = 0
    isLeftStart = True
    
    while current <= n:
        current += w
        if current < num:
            answer -= 1
        else:
            if isLeftStart:
                if num % w == 0:
                    index = w - 1
                else:
                    index = num % w -1
            else:
                if num % w == 0:
                    index = 0
                else:
                    index = w-(num % w)
            break
        isLeftStart = not isLeftStart
            
    isLeftStart = (n // w) % 2 == 0
    
    if n % w == 0:
        return answer
    
    if isLeftStart:
        left = n % w -1
        if left >= index:
            answer += 1
    else:
        left = w-n%w -1
        if left < index:
            answer += 1

    return answer 