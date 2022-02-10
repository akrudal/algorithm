def solution(array, commands):
    answer = []
    
    for value in commands:
        i=value[0]
        j=value[1]
        k=value[2]
        sortArray=sorted(array[i-1:j])
        answer.append(sortArray[k-1])
    return answer