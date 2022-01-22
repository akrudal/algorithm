def solution(genres, plays):
    answer = []
    
    songs={e:[] for e in set(genres)}
    
    for e in zip(genres,plays,range(len(plays))):
        songs[e[0]].append([e[1],e[2]])
    
    genreSort=sorted(list(songs.keys()),key=lambda x:sum(map(lambda y:y[0],songs[x])),reverse=True)
    
    for genre in genreSort:
        temp=[e[1] for e in sorted(songs[genre],key=lambda x:x[0],reverse=True)]
        answer+=temp[:2]
        
    return answer
