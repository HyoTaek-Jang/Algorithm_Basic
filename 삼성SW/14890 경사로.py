M, L = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

answer = 0


def isRoad(line):
    global answer
    result = checkLine(line)
    if result:
        answer += 1


def checkLine(line):
    history = [False] * len(line)
    prev = line[0]
    prevCnt = 0
    flag = -1
    for idx in range(len(line)):
        cur = line[idx]
        if cur == prev:
            prevCnt += 1
            if flag == 1 and prevCnt == L:
                for i in range(idx, idx - L, -1):
                    if history[i]:
                        return False
                    history[i] = True
            continue
        elif abs(prev - cur) > 1:
            return False
        elif cur > prev:
            if prevCnt < L:
                return False
            flag = 0
            for i in range(idx - 1, idx - 1 - L, -1):
                if history[i]:
                    return False
                history[i] = True
        else:
            if flag == 1 and prevCnt < L:
                return False
            flag = 1
        prev = cur
        prevCnt = 1
        if flag == 1 and prevCnt == L:
            for i in range(idx, idx - L, -1):
                if history[i]:
                    return False
                history[i] = True
    if flag == 1 and prevCnt < L:
        return False
    return True


def makeColLine(table, col):
    temp = []
    for i in range(len(table)):
        temp.append(table[i][col])
    return temp


for i in range(M):
    isRoad(table[i])
    isRoad(makeColLine(table, i))

print(answer)

