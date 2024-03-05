def solution(people, limit):
    answer = 0
    
    people.sort(reverse = True)
    minimum_index = -1
    
    for i in range(0, len(people)):
        if people[i] + people[minimum_index] <= limit:
            minimum_index -= 1
            
        answer += 1
        
        if i >= len(people) + minimum_index:
            break
    
    return answer