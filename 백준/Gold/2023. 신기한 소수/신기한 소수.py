N = int(input())

primeNumbers = [2, 3, 5, 7]
lastNumbers = [1, 3, 7, 9]


# 1의 자리 수 조기 리턴
if N == 1:
    for primeNumber in primeNumbers:
        print(primeNumber)
    exit()
    
def isPrime(num):
    for n in range(2,round(num/2) +1):
        if num % n == 0:
            return False
    return True

# 끝자리수가 1,3,7,9로 끝나는 체크리스트를 만든다.
def makeCheckList():
    checkList = []
    for primeNumber in primeNumbers:
        for lastNumber in lastNumbers:
            temp = primeNumber * 10 + lastNumber
            checkList.append(temp)
    return checkList

# 2자리 수 ~ 8자리 수
def findPrime(position):
    changePrimeNumbers = []
    checkList = makeCheckList()
    for i in checkList:
        if isPrime(i):
            changePrimeNumbers.append(i)
    return changePrimeNumbers

for i in range(2, N+1):
    primeNumbers = findPrime(i)

for primeNumber in primeNumbers:
    print(primeNumber)
    
    
    