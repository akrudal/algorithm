n, s = map(int, input().split())
n_list = list(map(int, input().split()))

subsets = [[]]
for num in n_list:
    size = len(subsets)
    for y in range(size):
        subsets.append(subsets[y]+[num])

count = 0     
for value in subsets:
    if sum(value) == s and len(value) != 0:
        count+=1
print(count)