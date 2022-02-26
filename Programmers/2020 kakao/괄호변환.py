def solution(p):
    if isRight(p):
        return p
    answer = fir(p)

    return answer


def isRight(p):
    leftCnt = 0
    for cur in list(p):
        if cur == "(":
            leftCnt += 1
        else:
            leftCnt -= 1
        if leftCnt < 0:
            return False
    return True


def fir(w):
    if len(w) == 0:
        return ''
    return sec(w)


def sec(p):
    leftCnt = 0
    rightCnt = 0
    for i in p:
        if i == "(":
            leftCnt += 1
        else:
            rightCnt += 1
        if leftCnt == rightCnt:
            break
    cut = leftCnt + rightCnt
    u = p[:cut]
    v = p[cut:]
    return thr(u, v)


def thr(u, v):
    if isRight(u):
        v = fir(v)
        return u + v
    else:
        v = fir(v)
        temp = "(" + v + ")"
        u = list(u)
        for idx in range(1, len(u) - 1):
            if u[idx] == "(":
                temp += ")"
            else:
                temp += "("
        return temp