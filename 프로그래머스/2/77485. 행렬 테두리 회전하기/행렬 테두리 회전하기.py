def solution(rows, columns, queries):
    answer = []
    
    board = [[i*columns + j +1 for j in range(columns)] for i in range(rows)]

    for query in queries:
        changedBoard = [i.copy() for i in board]

        minimum = rows * columns
        for row in range(query[0]-1, query[2]):
            for col in range(query[1]-1, query[3]):
                if row == query[0]-1:
                    if col == query[3] - 1:
                        changedBoard[row+1][col] = board[row][col]
                    else:
                        changedBoard[row][col+1] = board[row][col]
                    minimum = min(board[row][col], minimum)
                    
                elif col == query[1]-1:
                    if row == query[0] - 1:
                        changedBoard[row][col+1] = board[row][col]
                    else:
                        changedBoard[row-1][col] = board[row][col]
                    minimum = min(board[row][col], minimum)
                    
                elif row == query[2]-1:
                    if col == query[1] - 1:
                        changedBoard[row-1][col] = board[row][col]
                    else:
                        changedBoard[row][col-1] = board[row][col]
                    minimum = min(board[row][col], minimum)
                    
                elif col == query[3]-1:
                    if row == query[2] - 1:
                        changedBoard[row][col-1] = board[row][col]
                    else:
                        changedBoard[row+1][col] = board[row][col]
                    minimum = min(board[row][col], minimum)
        
        board = changedBoard
        answer.append(minimum)

    return answer