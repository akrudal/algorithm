import copy

def solution(arr):
    answer = [0,0]
    length = len(arr)
    size = length
    checked = [[False] * length for _ in range(length)]
    
    while(size > 0):
        sumSize = length // size
        summ = [[0] * sumSize for _ in range(sumSize)]
        for i in range(length):
            for j in range(length):
                if checked[i][j]: continue
                summ[i // size][j // size] += arr[i][j]

        for i in range(sumSize):
            for j in range(sumSize):
                if summ[i][j] == 0 and not checked[i * size][j * size]:
                    answer[0] += 1
                elif summ[i][j] == 1 * size * size and not checked[i * size][j * size]:
                    answer[1] += 1
                    
        for i in range(length):
            for j in range(length):
                if 0 == summ[i // size][j // size] and not checked[i][j]:
                    checked[i][j] = True
                elif summ[i // size][j // size] == 1 * size * size and not checked[i][j]:
                    checked[i][j] = True
        size //= 2

    for i in range(length):
        for j in range(length):
            if checked[i][j]: continue
            answer[arr[i][j]] += 1
            
    return answer