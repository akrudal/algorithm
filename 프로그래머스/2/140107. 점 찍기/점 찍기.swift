import Foundation

func solution(_ k:Int, _ d:Int) -> Int64 {
    var answer = 0
    
    for x in stride(from: 0, through: d, by: k) {
        let y = Int(sqrt(Double(d * d - x * x)))
        answer += y / k
    }
    answer += d / k + 1
    return Int64(answer)
}