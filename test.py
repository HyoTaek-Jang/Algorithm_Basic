def solution(strings, n):
    temp = sorted(strings, key=lambda x: x[n:])
    # 인덱스 같은 애들 정렬
    targetList = []
    for i in temp:
        if not i[n] in targetList:
            targetList += i[n]

    sortList = [[] for _ in range(len(targetList))]

    print(sortList)
    for i in temp:
        sortList[targetList.index(i[n])].append(i)

    print(sortList)
    answer = ''
    return answer
solution(['sum','asdf','vcxzv', "dcabvabs","auasdf"], 2)