from collections import deque

def solution(k, score):
    answer = []
    deque = []
    
    for i in range(0, min(len(score),k)):
        deque.append(score[i])
        answer.append(min(deque))
    
    deque = sorted(deque)
    
    for i in range(k, len(score)):
        if len(deque) == len(score): break
        deque.append(score[i])
        if score[i] > deque[-1]:
            deque = deque[1:k+1]
        else:
            deque = sorted(deque)[1:k+1]
        
        answer.append(deque[0])
    return answer