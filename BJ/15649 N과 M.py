N, M = map(int, input().split())
# 1~N까지 숫자를 M개 개수 수열
number = list(range(1, N + 1))


def makeAnswer(current, history):
    for i in number:
        if len(current) == M:
            print(' '.join(map(str, current)))
            return
        if i in current or len(current) > M:
            continue
        current.append(i)
        history = makeAnswer(current, history)
        current.pop()
    return

makeAnswer([], [])

