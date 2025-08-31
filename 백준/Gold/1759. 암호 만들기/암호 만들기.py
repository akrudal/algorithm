import sys

input = sys.stdin.readline

l,c = map(int, input().split())
alpha = sorted(list(map(str, input().split())))



def backTracking(idx, temp, alpha):
    if len(alpha) == l:
        gather = 0
        vowel = 0
        for ss in alpha:
            if ss in ["a", "e", "i", "o", "u"]:
                gather += 1
            else:
                vowel += 1
        if gather >= 1 and vowel >= 2:
            print(alpha)
        return
    
    for i in range(idx, len(temp)):
        backTracking(i + 1, temp, alpha + temp[i])


backTracking(0, alpha, "")