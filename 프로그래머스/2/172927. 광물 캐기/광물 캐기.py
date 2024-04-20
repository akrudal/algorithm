def countTired(minerals, i, pick):
    answer = 0
    for j in range(5):
        if i*5+j >= len(minerals):
            return answer
        if pick == 'diamond':
            answer += 1
        elif pick == 'iron':
            if minerals[i*5+j] == 'diamond':
                answer += 5
            else:
                answer += 1
        else:
            if minerals[i*5+j] == 'diamond':
                answer += 25
            elif minerals[i*5+j] == 'iron':
                answer += 5
            else:
                answer += 1
    return answer

def solution(picks, minerals):
    answer = 0
    
    length = len(minerals)
    counts = [[i,0] for i in range(length//5 + 1 if length % 5 != 0 else length//5)]
    
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            counts[i//5][1] += 25
        elif minerals[i] == 'iron':
            counts[i//5][1] += 5
        else:
            counts[i//5][1] += 1

    counts.sort(key = lambda x: -x[1])
    
    sortedPicks = []
    sortedPicks.extend(['diamond'] * picks[0])
    sortedPicks.extend(['iron'] * picks[1])
    sortedPicks.extend(['stone'] * picks[2])
    
    for i,count in enumerate(counts):
        count[1] = i
        
    counts.sort(key = lambda x: x[0])

    pickCount = 0
    for count in counts:
        if pickCount >= len(sortedPicks):
            return answer
        if count[1] >= len(sortedPicks):
            pick = sortedPicks[0]
            answer += countTired(minerals, count[0], pick)
        else:
            pick = sortedPicks[count[1]]
            answer += countTired(minerals, count[0], pick)
        pickCount += 1
                
    return answer