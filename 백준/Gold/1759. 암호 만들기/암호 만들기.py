모음 = {"a", "e", "i", "o", "u"}
stack = []
alphabets = []
# 서로 다른 L개, 최소 1개의 모음과 최소 두 개의 자음

def make_combinations(m, n, nindex):
    length=len(stack)
    
    # print("current", nindex, stack, length, n)
    
    # 예외 조건: 배열의 인덱스를 넘을 경우는 제외
    if nindex > m: return
    # 종료 조건: C개 중 L만큼 뽑았을 때
    if length == n:
        # 모음이 1개라도 없을 경우는 제외
        if (not (set(stack) & 모음) or (len(set(stack) - 모음) < 2)): 
            return
        
        print("".join(stack))
        return

    for i, a in enumerate(alphabets[min(nindex, m-1): ]):
        stack.append(a)
        make_combinations(m, n, nindex+1)
        stack.pop()
            
        nindex += 1
            
def main():
    global stack, alphabets
    L, C = map(int, input().split())
    alphabets = sorted(input().split())
    
    for i in range(C):
        stack.append(alphabets[i])
        make_combinations(C, L, i+1)
        stack = []
    
main()