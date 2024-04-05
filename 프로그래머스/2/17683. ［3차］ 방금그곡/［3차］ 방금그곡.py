import re

def solution(m, musicinfos):
    answer = []
    
    m = m.replace('A#', 'a').replace('B#','b').replace('C#','c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('G#','g')

    for musicinfo in musicinfos:
        music = musicinfo.split(",")
        
        sh, sm = map(int, music[0].split(":"))
        fh, fm = map(int, music[1].split(":"))
        
        playTime = (fh * 60 + fm) - (sh * 60 + sm)

        music[3] = music[3].replace('A#', 'a').replace('B#','b').replace('C#','c').replace('D#', 'd').replace('E#', 'e').replace('F#', 'f').replace('G#','g')
        playedNotes = music[3] * (playTime // len(music[3])) + music[3][:(playTime % len(music[3]))]
        if re.search(m, playedNotes):
            answer.append((music[2], playTime))
    
    if not answer:
        return '(None)'
    else:
        answer.sort(key = lambda x: -x[1])
    return answer[0][0]