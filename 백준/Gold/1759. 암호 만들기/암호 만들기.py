r, n = map(int, input().split())
n_list = sorted(list(input().split()))

result = []

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_count = 1
consonants_count = 0

def recursive(x):
    global vowels_count, consonants_count
    # print(result, vowels_count)
    if len(result) == r and vowels_count <= 0 and consonants_count >= 2:
        for c in result:
            print(c, end = '')
        print()
        return
    else:
        for i in range(x, n):
                result.append(n_list[i])
                if n_list[i] in vowels:
                    vowels_count -= 1
                else:
                    consonants_count +=1
                # print(result, n_list[i], vowels_count)
                recursive(i+1)
                result.pop()
                if n_list[i] in vowels:
                    vowels_count += 1
                else:
                    consonants_count -= 1
            
recursive(0)
