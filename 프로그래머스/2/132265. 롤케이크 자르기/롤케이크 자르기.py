def solution(toppings):
    answer = 0
    
    dic = {}
    for topping in toppings:
        if topping in dic:
            dic[topping] += 1
        else:
            dic[topping] = 1
    
    left = set()
    right = set(toppings)
    for topping in toppings:
        left.add(topping)
        
        if topping in dic:
            dic[topping] -= 1
            if dic[topping] == 0:
                del dic[topping]
                right.remove(topping)
                
        if len(left) == len(right): answer += 1
    
    return answer