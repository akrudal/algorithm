def canChange(before, after):
    count = 0
    for i in range(len(before)):
        if before[i] != after[i]:
            count += 1
    
    return count == 1

def solution(begin, target, words):
    N = len(words)
    answer = []
    visited = [False] * N
    

    def dfs(word, count):
        
        if word == target: 
            answer.append(count)
            return
    
        for next in range(N):
            if not visited[next] and canChange(word, words[next]):
                visited[next] = True
                dfs(words[next], count+1)
                visited[next] = False
    

    dfs(begin, 0)
    
    if not answer: return 0
    return min(answer)