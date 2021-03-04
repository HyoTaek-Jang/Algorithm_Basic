import collections


def solution(progresses, speeds):
    answer = []
    progresses = collections.deque(progresses)
    speeds = collections.deque(speeds)

    while (progresses):
        result = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            result += 1
        if result != 0: answer.append(result)

        for i in range(len(progresses)):
            progresses[i] += speeds[i]

    return answer