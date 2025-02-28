def solution(video_len, pos, op_start, op_end, commands):
    current = makeSecond(pos)
    op_start_sec = makeSecond(op_start)
    op_end_sec = makeSecond(op_end)
    max_sec = makeSecond(video_len)
    
    for command in commands:
        if op_start_sec <= current <= op_end_sec:
            current = op_end_sec
            
        if command == "prev":
            current -= 10

            if current < 0:
                current = 0
        elif command == "next":
            current += 10

            if current > max_sec:
                current = max_sec

    if op_start_sec <= current <= op_end_sec:
        current = op_end_sec
    
    return makeTime(current)

def makeSecond(time):
    minute, sec = map(int, time.split(":"))
    
    return minute * 60 + sec
    
def makeTime(sec):
    minute = sec // 60
    second = sec % 60
    
    str_minute = "0" + str(minute) if minute < 10 else str(minute)
    str_second = "0" + str(second) if second < 10 else str(second)
    
    return str_minute+":"+str_second
    