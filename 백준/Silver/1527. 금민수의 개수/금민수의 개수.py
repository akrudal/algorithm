a,b = map(int,input().split())
q = [4,7]
ans = 0

while len(q) > 1:
    f = q[0]
    q.pop(0)
    
    if f<=b:
        if a<=f:
            ans+=1
        q.append(f*10+4)
        q.append(f*10+7)

print(ans)