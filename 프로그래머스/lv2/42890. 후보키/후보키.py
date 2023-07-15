def returnSubset(arr):
    subsets = [[]]

    for num in arr:
        size = len(subsets)
        for y in range(size):
            subsets.append(subsets[y]+[num])
    return subsets

def solution(relation):
    # 후보키(Candidate Key)
    # 관계 데이터베이스에서 relation의 tuple을 유일하게 실별할 수 있는 attribute 중 다음 두 조건을 만족하는 것을 후보키라고 한다.
    # 유일성: relation에 있는 모든 튜플에 대해 유일하게 식별되어야한다.
    # 최소성: 유일성을 가진 키를 구성하는 attribute 중 하나라도 제외하는 경우 유일성의 깨진다.
    # 즉, relation의 모든 tuple을 유일하게 식별하는데 꼭 필요한 속성들로 구성되어야 한다.
    nums = [i for i in range(len(relation[0]))]
    subsets = returnSubset(nums)

    temp_data = []
    answer = []
    for subset in subsets:
        for r in relation:
            data = ""
            for s in subset:
                data += r[s]

            if not data in temp_data:
                temp_data.append(data)
            else:
                break

        if len(temp_data) == len(relation):
            answer.append(subset)
        temp_data = []
    
    sub_answer = []
    for a in answer:
        isMinimality = True
        for check in sub_answer:
            if check in returnSubset(a):
                isMinimality = False
        if isMinimality:
            sub_answer.append(a)
    return len(sub_answer)