import math

def solution(n):
    jump = 0
    while(n > 0):
        if n % 2 == 0:
            n = n / 2
        else:
            jump += 1
            n = n - 1
    return jump
    