def search(x, y, n, trees):
    checked = [False] * n
    checked[x-1] = True
    checked[y-1] = True
    
    first = trees[x][:]
    firstCount = 0

    while first:
        q = first.pop(0)
        if checked[q-1]: continue
        first.extend(trees[q])
        checked[q-1] = True
        firstCount += 1
    return firstCount


def solution(n, wires):
    answer = 100
    
    trees = {}
    for wire in wires:
        if wire[0] in trees:
            trees[wire[0]].append(wire[1])
        else:
            trees[wire[0]] = [wire[1]]
            
        if wire[1] in trees:
            trees[wire[1]].append(wire[0])
        else:
            trees[wire[1]] = [wire[0]]
    
    for wire in wires:
        a = search(wire[0], wire[1], n, trees)
        b = search(wire[1], wire[0], n, trees)
        
        a, b= (a, b) if a > b else (b, a)
        answer = min(answer,a-b)
        
    return answer