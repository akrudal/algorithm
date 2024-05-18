def isPalindrome(arr):
    mid = len(arr) // 2
    
    index = 0
    while(index < mid):
        if arr[index] != arr[-index-1]:
            return 0
        index += 1
    return 1

def solution(length, board, i, j):
    answer = 0
    if j + length - 1 < 8:
        answer += isPalindrome(board[i][j:j+length])
    
    if i + length - 1 < 8:
        arr = [board[k][j] for k in range(i, i+length)]
        answer += isPalindrome(arr)
        
    return answer

for t in range(10):
    length = int(input())
    board = [[c for c in input()] for i in range(8)]
    answer = 0
    for i in range(8):
        for j in range(8):
            answer += solution(length, board, i, j)
    print(f"#{t+1} {answer}")