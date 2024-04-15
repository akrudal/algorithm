import Foundation

struct Point {
    var x: Int
    var y: Int
    var z: Int
}

struct Deque<T> {
    private var array = [T]()
    
    var isEmpty: Bool {
        return array.isEmpty
    }
    
    mutating func enqueue(_ element: T) {
        array.append(element)
    }
    
    mutating func dequeue() -> T? {
        guard !isEmpty else { return nil }
        return array.removeFirst()
    }
}

func bfs(board: [String], x: Int, y: Int) -> Int {
    let N = board.count
    let M = board[0].count
    var checked = [[Bool]](repeating: [Bool](repeating: false, count: M), count: N)
    var queue = Deque<Point>()
    queue.enqueue(Point(x: x, y: y, z: 0))
    
    while !queue.isEmpty {
        guard let current = queue.dequeue() else { continue }
        let x = current.x
        let y = current.y
        let z = current.z
        
        if x < 0 || x >= N || y < 0 || y >= M || checked[x][y] { continue }
        if board[x][board[x].index(board[x].startIndex, offsetBy: y)] == "G" {
            return z
        }
        
        var up = -1, down = 1, left = -1, right = 1
        
        while 0 <= x + up && x + up < N && board[x + up][board[x + up].index(board[x + up].startIndex, offsetBy: y)] != "D" {
            up -= 1
        }
        queue.enqueue(Point(x: x + up + 1, y: y, z: z + 1))
        
        while 0 <= x + down && x + down < N && board[x + down][board[x + down].index(board[x + down].startIndex, offsetBy: y)] != "D" {
            down += 1
        }
        queue.enqueue(Point(x: x + down - 1, y: y, z: z + 1))
        
        while 0 <= y + left && y + left < M && board[x][board[x].index(board[x].startIndex, offsetBy: y + left)] != "D" {
            left -= 1
        }
        queue.enqueue(Point(x: x, y: y + left + 1, z: z + 1))
        
        while 0 <= y + right && y + right < M && board[x][board[x].index(board[x].startIndex, offsetBy: y + right)] != "D" {
            right += 1
        }
        queue.enqueue(Point(x: x, y: y + right - 1, z: z + 1))
        
        checked[x][y] = true
    }
    
    return -1
}

func solution(_ board: [String]) -> Int {
    for i in 0..<board.count {
        for j in 0..<board[0].count {
            if board[i][board[i].index(board[i].startIndex, offsetBy: j)] == "R" {
                return bfs(board: board, x: i, y: j)
            }
        }
    }
    return -1
}
