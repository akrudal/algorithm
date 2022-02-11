def solution(answers):
    answer = []
    
    person1=[1,2,3,4,5]
    person2=[2,1,2,3,2,4,2,5]
    person3=[3,3,1,1,2,2,4,4,5,5]
    
    while(len(answers)>len(person1)):
        person1.extend(person1)
    while(len(answers)>len(person2)):
        person2.extend(person2)
    while(len(answers)>len(person3)):
        person3.extend(person3)
    
    count=[[1,0],[2,0],[3,0]]
    for i in range(len(answers)):
        if(answers[i]==person1[i]):
            count[0][1]+=1
        if(answers[i]==person2[i]):
            count[1][1]+=1
        if(answers[i]==person3[i]):
            count[2][1]+=1
    
    count.sort(key=lambda x:(-x[1],x[0]))
    answer.append(count[0][0])
    
    if(count[1][1]==count[0][1]):
        answer.append(count[1][0])
    if(count[2][1]==count[0][1]):
        answer.append(count[2][0])
        
    return answer