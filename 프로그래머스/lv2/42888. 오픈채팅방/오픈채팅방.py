def solution(records):
    answer = []
    
    users = {}
    # 들어온 기록
    for record in records:
        temp = record.split()
        if len(temp) == 3:
            uid = temp[1]   
            name = temp[2]
        
            users[uid] = name
    
    answer = []
    for record in records:
        temp = record.split()
        if temp[0] == "Enter":
            answer.append(users[temp[1]]+"님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(users[temp[1]]+"님이 나갔습니다.")
    return answer