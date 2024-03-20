def solution(numbers):
    answer = []
    
    for number in numbers:
        binary = format(number, 'b')
        if binary[-1] == '0':
            answer.append(number + 1)
            continue
        else:
            count = ""
            for i in range(0, len(binary)):
                if binary[-i-1] == '0':
                    break
                count += "1"
            answer.append(number + 2 ** (len(count) -1))
    return answer