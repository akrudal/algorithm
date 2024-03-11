from collections import deque

def solution(numbers, target):
    answer = 0
    dx = [n for n in numbers] + [-n for n in numbers]
    
    q = deque([(dx[0], 0), (-dx[0], 0)])
    while q:
        num, i = q.popleft()
        
        if i+1 == len(numbers):
            if num == target: answer += 1
            continue
        
        q.append((num + dx[i+1], i+1))
        q.append((num - dx[i+1], i+1))
        
    return answer