def convert(n, k):
    result = ""

    while(n > 0):
        result += str(n % k)
        n //= k
    
    result = result[::-1]
    return result

def isPrime(n):
    n = int(n)
    for x in range(2, int(n**(0.5))+1):
        if n % x == 0: return False
    return True

def solution(n, k):
    
    # n -> k로 변환
    n = str(n) if k == 10 else convert(n, k)
    n = n.split('0')
    answer = len(n)
    
    for num in n:
        if num == '1' or num == '' or not isPrime(num): answer -= 1
    
    return answer