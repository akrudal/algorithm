A, B = map(int, input().split())

num = 1
count = num
result = 0
for i in range(B):
    
    count -=1
    if i >= A -1:
        result += num
    
    if count == 0:
        num += 1
        count = num
        
print(result)