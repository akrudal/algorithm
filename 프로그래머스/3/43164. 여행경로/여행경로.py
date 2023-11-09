from collections import defaultdict

def solution(tickets):
    tickets_dict = defaultdict(list)

    for start, end in tickets:
        tickets_dict[start].append(end)

    for key in tickets_dict.keys():
        tickets_dict[key].sort(reverse = True)
    
    answer = []
    path = ["ICN"]
    
    while path:
        now = path[-1]
        
        if now not in tickets_dict or len(tickets_dict[now]) == 0:
            answer.append(path.pop())
        else:
            path.append(tickets_dict[now].pop())
    
    return answer[::-1]