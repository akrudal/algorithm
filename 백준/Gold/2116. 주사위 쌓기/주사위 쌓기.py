n = int(input())
dices = [list(map(int, input().split())) for _ in range(n)]
dices_dict = {1:6, 2:4, 3:5, 4:2, 5:3, 6:1}

def get_max(exclude, array):
    maximum = 0
    for i in range(len(array)):
        if i == exclude or i == dices_dict[exclude+1]-1:
            continue
        else:
            maximum = max(maximum,array[i])
    return maximum

maximum = 0
for i in range(6):
    top = dices[0][dices_dict[i+1]-1]
    temp = get_max(i, dices[0])
    for dice in dices[1:]:
        index = dice.index(top)
        temp += get_max(index ,dice)
        top = dice[dices_dict[index+1]-1]
    maximum = max(maximum, temp)
print(maximum)