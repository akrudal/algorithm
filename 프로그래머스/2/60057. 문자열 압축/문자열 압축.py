def solution(s):
    answer = len(s)
    
    size = 1
    while(size <= (len(s) // 2)):
        length, count = 0, 0
        pattern = s[0:size]
        
        for i in range(0,len(s),size):
            if s[i:i+size] == pattern:
                count += 1
            else:
                if count == 1:
                    length += len(pattern)
                else:
                    length += len(str(count)) + len(pattern)
                
                pattern = s[i:i+size]
                count = 1
                
        length += len(pattern) if count == 1 else len(str(count)) + len(pattern)
        answer = min(answer, length)
        size += 1
        
    return answer