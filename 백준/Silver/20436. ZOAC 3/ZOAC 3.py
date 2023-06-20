keyboard = [["q","w","e","r","t","y","u","i","o","p"],
    ["a","s","d","f","g","h","j","k","l"],
    ["z","x","c","v","b","n","m"]]


sl,sr = input().split()
state = input()

def getLocation(i):
    for row in range(len(keyboard)):
        try:
            temp = keyboard[row].index(i)
            return row,temp
        except:
            continue

    return x,y

lx, ly = getLocation(sl)
rx, ry = getLocation(sr)
count = 0
for i in range(len(state)):
    x,y = getLocation(state[i])
    if ((x == 0 or x ==1) and y<=4) or (x == 2 and y<= 3):
        count += abs(lx - x) + abs(ly - y)
        lx, ly = x, y
    else:
        count += abs(rx - x) + abs(ry - y)
        rx , ry = x, y
    count += 1
print(count)