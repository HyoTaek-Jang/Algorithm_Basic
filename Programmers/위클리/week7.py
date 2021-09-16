def solution(enter, leave):
    length = len(enter)
    answer = [0 for _ in range(length)]

    room = []
    enterIdx = 0
    leaveIdx = 0
    while not (enterIdx == leaveIdx == length):

        if (enterIdx != length):
            room.append(enter[enterIdx])
            for curIdx in range(len(room) - 1):
                answer[enter[enterIdx]-1] += 1
                answer[room[curIdx] - 1] += 1
            enterIdx += 1

        if leave[leaveIdx] in room:
            room.remove(leave[leaveIdx])
            leaveIdx += 1

    for curAnswer in answer:
        curAnswer /= 2

    return answer

