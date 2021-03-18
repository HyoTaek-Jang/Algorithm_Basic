def solution(N, stages):
    checkStage = [0 for i in range(N + 1)]

    for i in stages:
        for j in range(0, i):
            checkStage[j] += 1

    for k in range(0, N):
        if checkStage[k + 1] == 0:
            break
        checkStage[k] = 1 - (checkStage[k + 1] / checkStage[k])

    checkStage = list(enumerate(checkStage[:N]))
    checkStage.sort(reverse=True, key=lambda x: x[1])

    answer = [j[0] + 1 for j in checkStage]
    return answer