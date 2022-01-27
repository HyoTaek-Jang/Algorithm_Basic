from collections import deque


def solution(priorities, location):
    queue = deque()

    for idx in range(len(priorities)):
        queue.append((priorities[idx], idx))

    answer = 0
    while True:
        big = max(queue)
        cur = queue.popleft()

        if big[0] == cur[0] and cur[1] == location:
            return answer + 1
        elif big[0] == cur[0]:
            answer += 1
        else:
            queue.append(cur)