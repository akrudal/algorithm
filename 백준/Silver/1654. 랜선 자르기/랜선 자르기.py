K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start = 1
end = max(lines)

def binary_search(start, end, array):

    while(start <= end):
        count = 0
        mid = (start + end) // 2
        
        for line in lines:
            count += line // mid
            
        if count >= N:
            start = mid + 1
        else:
            end = mid - 1
    
    
    return end
    
print(binary_search(start,end,lines))