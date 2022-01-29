def solution(n, computers):
    connect = {}

    for idx in range(len(computers)):
        connect[idx + 1] = []
        for i in range(n):
            if computers[idx][i] == 1:
                connect[idx + 1].append(i + 1)

    answer = 0
    for idx in connect:
        if connect[idx]:
            answer += 1

        temp = []
        while connect[idx]:
            temp.append(connect[idx].pop())

        while temp:
            cur = temp.pop()
            while connect[cur]:
                temp.append(connect[cur].pop())

    return answer