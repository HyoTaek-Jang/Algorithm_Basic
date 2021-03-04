def solution(answers):
    answer = []

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in [a, b, c]:
        i *= (len(answers) // len(i) + 1)

    count = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == a[i]:
            count[0] += 1
        if answers[i] == b[i]:
            count[1] += 1
        if answers[i] == c[i]:
            count[2] += 1

    for i in range(len(count)):
        if max(count) == count[i]:
            answer.append(i + 1)

    return answer