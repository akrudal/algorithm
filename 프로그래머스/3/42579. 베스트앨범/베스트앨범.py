def solution(genres, plays):
    answer = []

    genres_play_dict = {}
    genres_dict = {}
    
    for i in range(len(genres)):
        if genres[i] in genres_play_dict:
            genres_play_dict[genres[i]] += plays[i]
            genres_dict[genres[i]].append(i)
        else:
            genres_play_dict[genres[i]] = plays[i]
            genres_dict[genres[i]] = [i]
    
    sorted_genres = sorted(genres_play_dict, key=lambda x: -genres_play_dict[x])
    
    for genre in sorted_genres:
        genre_plays = []
        for num in genres_dict[genre]:
            genre_plays.append((num, plays[num]))
        
        genre_plays.sort(key=lambda x: -x[1])
        genre_plays = genre_plays[:2]
        
        for genre_play in genre_plays:
            answer.append(genre_play[0])
    return answer