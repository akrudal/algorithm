from collections import defaultdict
from itertools import combinations

def solution(clothes):
    answer = 0
    temp = 1
    
    for i in clothes:
       i[0],i[1]=i[1],i[0]
    
    myClothes=defaultdict(list)
    for k,v in clothes:
        myClothes[k].append(v)
    
    myList=[]
    for i in myClothes:
        myList.append(len(myClothes[i]))
    
    answer+=sum(myList)
    for i in range(2,len(myList)+1):
        for j in list(combinations(myList,i)):
            temp=1
            for k in j:
                temp*=k
            answer+=temp
    
    return answer