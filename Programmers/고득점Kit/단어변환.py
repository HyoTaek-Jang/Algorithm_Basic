from collections import deque


def solution(begin, target, words):
    if not target in words:
        return 0

    history = set()
    queue = deque()
    for word in words:
        if checkDiff(begin, word):
            queue.append([word, 1])
            history.add(word)

    while queue:
        cur = queue.popleft()
        if cur[0] == target:
            return cur[1]

        for word in words:
            if checkDiff(word, cur[0]) and not word in history:
                queue.append([word, cur[1] + 1])
                history.add(word)

    return 0


def checkDiff(a, b):
    cnt = 0
    for idx in range(len(a)):
        if a[idx] != b[idx]:
            cnt += 1
        if cnt > 1:
            return False
    return True