def solution(jobs):
    temp = []
    for job in jobs:
        temp.append((job[1], job[0]))

    temp.sort(key=lambda x: (x[0], x[1]))

    answer = []
    time = 0
    while len(temp):
        delete_idx = -1
        for idx in range(len(temp)):
            cur = temp[idx]
            if cur[1] <= time:
                time += cur[0]
                answer.append(time - cur[1])
                delete_idx = idx
                break
        if delete_idx == -1:
            time += 1
            continue
        temp.pop(delete_idx)

    return sum(answer) // len(answer)
