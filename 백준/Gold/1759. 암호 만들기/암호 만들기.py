모음 = {"a", "e", "i", "o", "u"}
stack = []
alphabets = []

def make_combinations(L, C, start, vowel_count, consonant_count):
    # 길이 L에 도달했을 때
    if len(stack) == L:
        # 최소 1개의 모음과, 최소 2개의 자음으로 이루어질 경우 정답 출력
        if vowel_count >= 1 and consonant_count >= 2:
            print("".join(stack))
        return

    for i in range(start, C):
        char = alphabets[i]
        stack.append(char)
        
        if char in 모음:
            make_combinations(L, C, i+1, vowel_count+1, consonant_count)
        else:
            make_combinations(L, C, i+1, vowel_count, consonant_count+1)
        
        stack.pop()

def main():
    global alphabets
    L, C = map(int, input().split())
    alphabets = sorted(input().split())
    make_combinations(L, C, 0, 0, 0)

main()
