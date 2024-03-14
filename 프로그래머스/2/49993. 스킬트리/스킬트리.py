def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for ss in skill_trees:
        stack = [s for s in skill[::-1]]
        
        for s in ss:
            if s in stack:
                if stack[-1] == s:
                    stack.pop()
                else:
                    answer -= 1
                    break
    return answer