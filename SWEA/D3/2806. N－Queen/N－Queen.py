T = int(input())

def isQueen(N, board):
    
    for row in range(N):
        col = -1
        for j in range(N):
            if board[row][j] == 1:
                if col != - 1: return 0
                col = j
        
        for k in range(N):
            if k != row and board[k][col] == 1:
                return 0
                
        for l in range(1, N):
            if row+l < N and col+l < N and board[row+l][col+l] == 1:
                return 0
                
            if row+l < N and col-l >=0 and board[row+l][col-l] == 1:
                return 0
                    
            if row-l >=0 and col+l <N and board[row-l][col+l] == 1:
                return 0
                
            if row-l >=0 and col-l >=0 and board[row-l][col-l] == 1:
                return 0

    return 1

def solution(N, depth, board, cols):
    answer = 0
    if depth == N:
        return isQueen(N, board)
    else:
        for i in range(N):
            board[depth][i] = 1
            if not i in cols:
                cols.append(i)
                answer += solution(N, depth+1, board, cols)
                cols.pop(-1)
            board[depth][i] = 0
    return answer

    
for i in range(T):
    N = int(input())
    
    board = [[0] * N for _ in range(N)]
    cols = []
    print(f"#{i+1} {solution(N, 0, board, cols)}")