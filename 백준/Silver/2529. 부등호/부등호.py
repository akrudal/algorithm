n = int(input())
inequalities = input().split()
m = n + 1

isFind = False
l = [i for i in range(9, -1, -1)]
selected = [0] * m
checked = [False ] * len(l)

def recursive(x):
    global isFind
    if isFind:
        return
    
    if x == m:
        if checkInequality(selected):
            isFind = True
            for value in selected:
                print(value, end='')
            return
    else:
        for (index,value) in enumerate(l):
            if not checked[index] and not isFind:
                selected[x] = value
                checked[index] = True
                recursive(x+1)
                checked[index] = False

def checkInequality(selected):
    for (index, inequality) in enumerate(inequalities):
        if inequality == "<":
            if selected[index] >= selected[index + 1]:
                return False
        else:
            if selected[index] <= selected[index + 1]:
                return False
    return True

result1 = recursive(0)

print()
l.sort()
checked = [False] * len(l)
isFind = False

result2 = recursive(0)