def search(x, y, place):
    dx = [1, 0, -1, 0]
    dy = [0, -1 ,0, 1]
    
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or nx >= 5 or ny<0 or ny >=5: continue
        if place[nx][ny] == 'P':
            return False

    dx = [1, 1, -1, -1]
    dy = [1, -1, 1, -1]
    
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5: continue
        
        if place[nx][ny] == 'P':
            if i == 0 and 0<=ny<4 and 1<=nx<5 and (place[nx][ny-1] == "O" or place[nx-1][ny] == "O"):
                return False
            
            if i == 1 and 1<=ny<5 and 1<=nx<5 and (place[nx][ny+1] == "O" or place[nx-1][ny] == "O"):
                return False

            if i == 2 and 1<=ny<5 and 0<=nx<4 and (place[nx][ny-1] == "O" or place[nx+1][ny] == "O"):
                return False
            
            if i == 3 and 0<=ny<4 and 0<=nx<4 and (place[nx][ny+1] == "O" or place[nx+1][ny] == "O"):
                return False
            
    dx = [2, -2, 0, 0]
    dy = [0, 0, -2, 2]
    
    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx <0 or nx >=5 or ny<0 or ny >= 5: continue
        
        if place[nx][ny] == "P":
            if i == 0 and 1<=nx<5 and place[nx-1][ny] == "O":
                return False
            if i == 1 and 0<=nx<4 and place[nx+1][ny] == "O":
                return False
            if i == 2 and 0<=ny<4 and place[nx][ny+1] == "O":
                return False
            if i == 3 and 1<=ny<5 and place[nx][ny-1] == "O":
                return False
            
    return True

def solution(places):
    answer = []
    
    places = [[[c for c in p] for p in place] for place in places]

    for place in places:
        can = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P" and not search(i, j, place):
                    can = False
                    break
            if not can:
                break
        if not can:
            answer.append(0)
        else:
            answer.append(1)

    return answer