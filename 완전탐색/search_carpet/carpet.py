def solution(brown, yellow):
    answer = []
    
    divisor=[]
    for i in range(1,yellow+1):
        if(yellow%i==0):
            if(i>=yellow/i):
                divisor.append((i,int(yellow/i)))
            else:
                divisor.append((int(yellow/i),i))
    
    for value in divisor:
        width=value[0]+2
        height=value[1]+2
        if(width*2+height*2-4==brown):
            answer=[width,height]
        
    return answer