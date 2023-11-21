N = int(input())
numbers = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))
operators = ["+", "-", "*", "/"]

def makeOperatorSorted():
    result = []
    for i in range(4):
        temp = [operators[i]] * operator_counts[i]
        result.extend(temp)
    return result

totalOperators = makeOperatorSorted()
visited = [False] * len(totalOperators)
minimum, maximum = 1000000000, -1000000000
selectedOperators = []

def calculateNumbers(selectedOperators):
    currentNumber = numbers[0]
    currentNumberIndex = 0
    
    for selectedOperator in selectedOperators:
        if selectedOperator == "+":
            currentNumber += numbers[currentNumberIndex + 1]
        elif selectedOperator == "-":
            currentNumber -= numbers[currentNumberIndex + 1]
        elif selectedOperator == "*":
            currentNumber *= numbers[currentNumberIndex + 1]
        else:
            if currentNumber < 0:
                currentNumber = (-currentNumber//numbers[currentNumberIndex+1]) * -1
            else:
                currentNumber //= numbers[currentNumberIndex + 1]
        
        currentNumberIndex += 1
    return currentNumber

# len(selectedOperators)개 중에 N-1개 뽑기 (순열)
def makeSelectedOperator(x):
    global minimum, maximum
    if x == N-1:
        temp = calculateNumbers(selectedOperators[:])
        if temp < minimum:
            minimum = temp
        if temp > maximum:
            maximum = temp
    else:
        for (index, operator) in enumerate(totalOperators):
            if not visited[index]:
                visited[index] = True
                selectedOperators.append(operator)
                makeSelectedOperator(x+1)
                visited[index] = False
                selectedOperators.pop()

makeSelectedOperator(0)
print(maximum)
print(minimum)