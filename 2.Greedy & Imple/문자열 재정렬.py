def solution():
    base_input = list(input())

    alpha = []
    number = 0

    for cur in base_input:
        if cur.isalpha():
            alpha.append(cur)
            continue
        number += int(cur)

    alpha.sort()
    print("".join(alpha) + str(number))


solution()
