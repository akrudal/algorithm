def solution(board):
    N, M = len(board), len(board[0])
    answer = board[0][0]

    for i in range(1,N):
        for j in range(1,M):
            if board[i][j] == 1:
                board[i][j] = 1+ min(board[i-1][j], board[i-1][j-1], board[i][j-1])
                
                answer = max(board[i][j], answer)

    return answer * answer