def solution(answers):
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for idx in range(len(students)):
        s = students[idx]
        mul = len(answers) // len(s)
        students[idx] = s * (mul + 1)

    answer = [[0, 1], [0, 2], [0, 3]]
    for idx in range(len(answers)):
        for s in range(len(students)):
            if students[s][idx] == answers[idx]:
                answer[s][0] += 1

    answer.sort(key=lambda x: (-x[0], x[1]))

    out = []
    temp = 0
    for a in answer:
        if temp > a[0]:
            break
        out.append(a[1])
        temp = a[0]
    return out