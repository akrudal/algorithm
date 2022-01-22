def solution(genres, plays):
    answer = []
    
    songs={}
    for i in range(len(genres)):
        if genres[i] in songs:
            songs[genres[i]].update({i:plays[i]})
        else :
            songs[genres[i]]={i:plays[i]}
    
    myList=[]
    
    for i in songs:
        songs[i].update({-1:sum(songs[i].values())})
        songs[i] = sorted(songs[i].items(), key = lambda item: item[1], reverse = True)
        if(len(songs[i])==2):
            songs[i][0],songs[i][1]=songs[i][1],songs[i][0]
        myList+=[songs[i]]

    myList.sort(reverse=True)

    for i in myList:
        if(len(i)==2):
            answer+=[i[1][0]]
        else:
            answer+=[i[1][0]]
            answer+=[i[2][0]]
    
    return answer