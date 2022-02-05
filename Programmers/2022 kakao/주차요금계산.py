def solution(fees, records):
    record_table = {}
    for r in records:
        r = r.split(" ")
        if r[2] == 'IN' and r[1] not in record_table:
            record_table[r[1]] = [r[0]]
        else:
            record_table[r[1]].append(r[0])

    keys = sorted(record_table.items())

    answer = []
    for key in keys:
        if len(key[1]) % 2 == 1:
            key[1].append("23:59")
        time = calcul(key[1])
        price = fees[1]
        if time - fees[0] > 0:
            price += ((time - fees[0]) // fees[2]) * fees[3]
            if (time - fees[0]) % fees[2] != 0:
                price += fees[3]
        answer.append(price)

    return answer


def calcul(times):
    time = 0

    for idx in range(len(times) // 2):
        i = times[idx * 2]
        o = times[idx * 2 + 1]
        i = list(map(int, i.split(":")))
        o = list(map(int, o.split(":")))

        time += (o[0] - i[0]) * 60
        time += (o[1] - i[1])

    return time