def solution(clothes):
    clothes_dict = {}
    for clothe in clothes:
        if clothe[1] in clothes_dict:
            clothes_dict[clothe[1]].add(clothe[0])
        else:
            clothes_dict[clothe[1]] = set([clothe[0]])
    
    if len(clothes_dict) == 1: return len(clothes)

    answer = 1
    for key in clothes_dict.keys():
        answer *= (len(clothes_dict[key]) + 1)
    
    answer -= 1
    return answer