def solution(dirs):
    paths = set()
    x, y = 0, 0
    directions = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    
    for d in dirs:
        nx = x + directions[d][0]
        ny = y + directions[d][1]
        
        print(x, y, nx, ny)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            paths.add((x, y, nx, ny))
            paths.add((nx, ny, x, y))
            
            x, y = nx, ny
    
    return len(paths) // 2