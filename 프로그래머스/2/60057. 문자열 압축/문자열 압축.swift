import Foundation

func solution(_ s: String) -> Int {
    var answer = s.count
    
    var size = 1
    while size <= s.count / 2 {
        var length = 0
        var count = 0
        var pattern = String(s.prefix(size))
        
        var i = 0
        while i < s.count {
            let startIndex = s.index(s.startIndex, offsetBy: i)
            let endIndex = s.index(s.startIndex, offsetBy: min(i + size,s.count))
            let subString = String(s[startIndex..<endIndex])
            
            if subString == pattern {
                count += 1
            } else {
                if count == 1 {
                    length += pattern.count
                } else {
                    length += String(count).count + pattern.count
                }
                
                pattern = subString
                count = 1
            }
            
            i += size
        }
        
        if count == 1 {
            length += pattern.count
        } else {
            length += String(count).count + pattern.count
        }
        
        answer = min(answer, length)
        size += 1
    }
    
    return answer
}