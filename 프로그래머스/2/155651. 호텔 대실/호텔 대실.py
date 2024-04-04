def timeCal(time1, time2):
    clean = 10
    h1,m1 = map(int, time1.split(":"))
    h2,m2 = map(int, time2.split(":"))
    
    time1 = h1 * 60 + m1 + clean
    time2 = h2 * 60 + m2
    
    if time1 <= time2:
        return True
    return False

def solution(book_time):
    book_time.sort(key = lambda x: (x[0], x[1]))
    rooms = [book_time[0]]
    
    for time in book_time[1:]:
        isFull = True
        for i in range(len(rooms)):
            if timeCal(rooms[i][1], time[0]):
                isFull = False
                rooms[i] = time
                break
        if isFull:
            rooms.append(time)

    return len(rooms)