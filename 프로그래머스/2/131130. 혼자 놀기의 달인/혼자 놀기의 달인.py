def dfs(start, cards, checked):
    result = 0
    stack = [start]
    
    while stack:
        index = stack.pop()
        
        checked[index] = True
        result += 1
        
        next_index = cards[index] -1
        if checked[next_index]: break
        stack.append(next_index)
        
    return result


def solution(cards):
    n = len(cards)
    checked = [False] * n
    results = []
    
    for i in range(n):
        if checked[i]: continue
        result = dfs(i, cards, checked)
        if result == n: return 0
        results.append(result)
        
    results.sort()
    
    return results[-1] * results[-2]