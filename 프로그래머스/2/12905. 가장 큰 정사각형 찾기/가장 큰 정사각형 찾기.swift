func solution(_ board: [[Int]]) -> Int {
    let N = board.count
    let M = board[0].count
    var answer = board[0][0]

    var mutableBoard = board

    for i in 1..<N {
        for j in 1..<M {
            if mutableBoard[i][j] == 1 {
                mutableBoard[i][j] = 1 + min(mutableBoard[i - 1][j], mutableBoard[i - 1][j - 1], mutableBoard[i][j - 1])
                answer = max(mutableBoard[i][j], answer)
            }
        }
    }

    return answer * answer
}