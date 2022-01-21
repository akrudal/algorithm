'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from collections import defaultdict

def solution(clothes):
    answer = 0
    temp = 1
    
    for i in clothes:
       i[0],i[1]=i[1],i[0]
    
    myClothes=defaultdict(list)
    for k,v in clothes:
        myClothes[k].append(v)

    for i in myClothes:
        if(len(myClothes)==1):
            answer=len(myClothes[i])
            return answer;
        else:
            temp*=len(myClothes[i])+1
    
    
    answer+=temp
    answer-=1
    
    return answer