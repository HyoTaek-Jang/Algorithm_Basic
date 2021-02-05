def solution(strings, n):
    answer = []

    # 1차 키 값으로 정렬
    temp = sorted(strings, key=lambda x: x[n:])

    # 2차로 키 값 같은 애들 묶어서 정렬
    targetList = []
    for i in temp:
        if not i[n] in targetList:
            targetList += i[n]

    sortList = [[] for _ in range(len(targetList))]

    for i in temp:
        sortList[targetList.index(i[n])].append(i)

    for i in sortList:
        i.sort()
        answer += i

    return answer