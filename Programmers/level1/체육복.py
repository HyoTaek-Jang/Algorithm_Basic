def solution(n, lost, reserve):
    check = lost[:]
    for i in check:
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)

    check = lost[:]

    for i in check:
        if i - 1 in reserve:
            reserve.remove(i - 1)
            lost.remove(i)
        elif i + 1 in reserve:
            reserve.remove(i + 1)
            lost.remove(i)

    answer = n - len(lost)
    return answer