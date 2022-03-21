def solution(L):
    answer = []

    for cur in L:
        cnt = 0
        insertIdx = -1
        for idx in range(len(answer)):
            if answer[idx][0] >= cur[0]:
                cnt += 1
            if cnt == cur[1]:
                insertIdx = idx+1
            if cnt > cur[1]:
                break

        if insertIdx != -1:
            answer.insert(insertIdx, cur)
        else:
            answer.append(cur)

    return answer


print(solution([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))