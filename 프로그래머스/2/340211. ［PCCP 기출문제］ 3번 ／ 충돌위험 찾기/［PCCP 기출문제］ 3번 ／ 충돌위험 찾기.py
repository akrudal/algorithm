def find_routes(fromm, to):
    route = [fromm[:]]
    
    while(fromm != to):
        if fromm[0] != to[0]:
            if fromm[0] > to[0]:
                fromm[0] -= 1
            else:
                fromm[0] += 1
        else:
            if fromm[1]> to[1]:
                fromm[1] -= 1
            else:
                fromm[1] += 1
        
        route.append(fromm[:])
    
    return route

def solution(points, routes):
    answer = 0
    
    n = len(points)
    x = len(routes)
    
    optimal_route = {}
    total_routes = [[] for _ in range(x)]

    for x,route in enumerate(routes):
        for j in range(len(route)-1):
            fromm = route[j]
            to = route[j+1]

            fromm_coor = points[fromm-1]
            to_coor = points[to-1]

            key = str(fromm)+"-"+str(to)
            if not key in optimal_route:
                optimal_route[key] = find_routes(fromm_coor[:], to_coor[:])
            
            if total_routes and total_routes[x]:
                if total_routes[x][-1] == optimal_route[key][0]:
                    total_routes[x].pop()
                
            total_routes[x].extend(optimal_route[key])
    
    time = 0
    while True:
        time_location = []
        for total_route in total_routes:
            if time >= len(total_route): continue
            time_location.append(total_route[time])
        
        crashed = set()
        for i in range(len(time_location)):
            for j in range(i+1, len(time_location)):
                if time_location[i] == time_location[j] and not ((time_location[i][0], time_location[i][1]) in crashed): 
                    answer += 1
                    crashed.add((time_location[i][0], time_location[i][1]))
                    
        
        time += 1
        if len(time_location) <= 1:
            break
    
    return answer


        