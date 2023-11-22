def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        # 큰 숫자를 만날 때 까지 stack에 index를 저장하고
        # 큰 숫자를 만났을 때 pop하면서 index에 뒷 큰수를 지정해주기
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer