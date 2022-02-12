import itertools
import math

def solution(numbers):
    answer = 0
    
    numbers=[int(char) for char in numbers]
    
    listNumbers=[]
    for i in range(1,len(numbers)+1):
        result = list(set(itertools.permutations(numbers,i)))
        for j in result:
            listNumbers.append((''.join(str(value) for value in j)))
    
    listNumbers=list(set(int(value) for value in listNumbers))
    listNumbers.sort()
    
    for value in listNumbers:
        check=False
        if(value<2):
            continue
        elif(value==2):
            answer+=1
            continue
        for num in range(2,int(math.sqrt(value) + 1)):
            if (value%num==0):
                check=True
                break
        if(check==False):
            print(value)
            answer+=1
    return answer
    
print(solution("17"))