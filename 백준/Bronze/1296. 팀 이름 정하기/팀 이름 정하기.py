import copy
from itertools import combinations

name = input()
N = int(input())
result = [('', 0)] * N

d = {'L': 0, 'O': 0, 'V': 0, 'E': 0}

for n in name:
    if n in d:
        d[n] += 1


for i in range(N):
    loveDict = copy.deepcopy(d)
    count = 1
    teamName = input()
    
    for c in teamName:
        if c in d:
            loveDict[c] += 1
    
    for combi in list(combinations(['L','O','V','E'], 2)):
        count *= (loveDict[combi[0]] + loveDict[combi[1]])

    result[i] = (teamName, count % 100)
    
        
print(sorted(result, key = lambda x: (-x[1], x[0]))[0][0])