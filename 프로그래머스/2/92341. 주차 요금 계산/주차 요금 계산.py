def calculate(fees, times):
    if len(times) % 2 != 0:
        times.append([23,59])

    total = 0
    for i in range(0, len(times), 2):
        total += (times[i+1][0] - times[i][0]) * 60
        total += (times[i+1][1] - times[i][1])

    if total  == 0: return 0
    elif total <= fees[0]: return fees[1]

    temp = (total - fees[0]) / fees[2] if (total - fees[0]) % fees[2] == 0 else (total-fees[0]) // fees[2] + 1
    return fees[1] + temp * fees[3]

def solution(fees, records):
    answer = []
    
    parkDict = {}
    for record in records:
        info = record.split(" ")
        
        if not info[1] in parkDict:
            parkDict[info[1]] = [list(map(int, info[0].split(":")))]
        else:
            parkDict[info[1]].append(list(map(int, info[0].split(":"))))
    
    for times in sorted(parkDict.keys()):
        answer.append(calculate(fees, parkDict[times]))
    return answer