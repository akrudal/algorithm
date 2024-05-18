T = int(input())

def solution(memory):
    answer = 0
    length = len(memory)
    isChange = False
    original = "0" * length
    
    for i in range(length):
        if isChange:
            if original[i] == memory[i]:
                isChange = False
                answer += 1
        else:
            if original[i] != memory[i]:
                isChange = True
                answer += 1
    
    return answer

for i in range(T):
    memory = input()
    print(f"#{i+1} {solution(memory)}")