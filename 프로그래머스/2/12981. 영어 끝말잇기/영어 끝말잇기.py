def solution(n, words):
    answer = []

    stack = [words[0]]
    
    for (index, word) in enumerate(words[1:]):
        if stack[-1][-1] != word[0] or word in stack:
            return [(index + 1) % n + 1, (index + 1) // n + 1]
        else:
            stack.append(word)

    return [0, 0]