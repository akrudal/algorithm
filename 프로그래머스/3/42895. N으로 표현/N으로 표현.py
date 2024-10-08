def solution(N, number):
    all_set = []
    
    for count in range(1, 9):
        partial_set = set()
        partial_set.add(int(str(N) * count))
        
        for i in range(count - 1):
            for num1 in all_set[i]:
                for num2 in all_set[-i-1]:
                    partial_set.add(num1+num2)
                    partial_set.add(num1-num2)
                    partial_set.add(num1*num2)
                    if num2 != 0 :
                        partial_set.add(num1/num2)
                    
        if number in partial_set:
            return count
        
        all_set.append(partial_set)
    return -1