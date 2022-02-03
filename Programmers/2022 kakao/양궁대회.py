import copy

answer = [-1]
score = 0


def solution(n, info):
    global answer

    lion = [0] * 11
    dfs(0, info, lion)

    return answer


def dfs(start, apech, lion):
    global answer
    global score

    remain = sum(apech) - sum(lion)
    if remain == 0 or start == 11:
        cur_score = countScore(apech, lion)
        if score < cur_score:
            score = cur_score
            if remain > 0:
                lion[-1] += remain
            answer = copy.deepcopy(lion)
        elif score == cur_score:
            for idx in range(10, -1, -1):
                if answer[idx] > lion[idx]:
                    break
                if answer[idx] < lion[idx]:
                    answer = copy.deepcopy(lion)
                    break
        return

    if apech[start] + 1 <= remain:
        lion[start] = apech[start] + 1
    dfs(start + 1, apech, lion)
    lion[start] = 0
    dfs(start + 1, apech, lion)


def countScore(apech, lion):
    apech_score = 0
    lion_score = 0
    for idx in range(len(apech)):
        if apech[idx] == 0 and lion[idx] == 0:
            continue
        elif apech[idx] < lion[idx]:
            lion_score += 10 - idx
        else:
            apech_score += 10 - idx

    if lion_score - apech_score <= 0:
        return -1
    return lion_score - apech_score