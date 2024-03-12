vowels = ['A', 'E', 'I', 'O', 'U']

def solution(word):

    d = {}
    index = 0
    for a in vowels:
        d[a] = index
        index += 1
        for b in vowels:
            d[a+b] = index
            index += 1
            for c in vowels:
                d[a+b+c] = index
                index += 1
                for e in vowels:
                    d[a+b+c+e] = index
                    index += 1
                    for f in vowels:
                        d[a+b+c+e+f] = index
                        index += 1  
    return d[word] + 1