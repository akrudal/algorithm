def solution(citations):
    answer = 0
    
    citations.sort()
    
    while True:
        count=0
        for j in range(len(citations)):
            if(answer<=citations[j]):
                count+=1
        if(count<answer):
            answer-=1
            break
        elif(count==answer):
            break
        answer+=1
    
    return answer