def solution(schedules, timelogs, startday):
    answer = 0
    
    n = len(schedules)
    
    for i in range(n):
        not_late = 0
        
        start_day = startday
        
        deadline = schedules[i] + 10
        if (deadline % 100) // 60 > 0 :
            deadline += 100
            deadline -= 60
            
        for timelog in timelogs[i]:
            if 6<=start_day<=7:
                start_day += 1
                continue
                
            if start_day > 7:
                start_day = 1
                
            if timelog <= deadline:
                not_late += 1
                
            start_day += 1
    
        if not_late >= 5:
            answer += 1
    return answer