answer = 1e9


def solution(s):
    global answer
    answer = len(s)
    for i in range(1, (len(s) // 2) + 1):
        calcul(i, s)

    return answer


def calcul(unit, s):
    global answer

    temp = ""
    last = s[0:unit]
    cnt = 1
    for cur in range(unit, len(s), unit):
        end = cur + unit
        if s[cur:end] == last:
            cnt += 1
        else:
            if cnt != 1:
                temp += str(cnt)
            temp += last
            cnt = 1
        last = s[cur:end]
    if cnt != 1:
        temp += str(cnt)
    temp += last

    answer = min(answer, len(temp))