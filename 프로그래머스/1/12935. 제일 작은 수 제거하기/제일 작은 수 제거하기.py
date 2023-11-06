def solution(arr):
    minimum = 1000000
    for value in arr:
        if minimum > value:
            minimum = value
    if len(arr) == 1:
        return [-1]
    else:
        arr.remove(minimum)
        return arr