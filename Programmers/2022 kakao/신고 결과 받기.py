def solution(id_list, report, k):
    table = {}
    temp = {}
    for user in id_list:
        table[user] = set()
        temp[user] = 0

    for cur in report:
        user, reported = cur.split(" ")
        table[reported].add(user)

    for key in table:
        if len(table[key]) >= k:
            for i in table[key]:
                temp[i] += 1

    answer = []
    for key in table:
        answer.append(temp[key])

    return answer