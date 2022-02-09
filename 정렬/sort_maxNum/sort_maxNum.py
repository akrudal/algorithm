def solution(numbers):
    answer = ''
    myNumbers=[]
    
    if numbers.count(0) == len(numbers): 
        answer = "0"
        return answer
    
    numbers.sort()
    for value in numbers:
        str_temp=str(value)*4
        str_temp=str_temp[:4]
        myNumbers.append([int(str_temp),len(str(value))])

    myNumbers.sort(key=lambda x:-x[0])
    
    for value in myNumbers:
        answer+=str(value[0])[:value[1]]
        
    return answer