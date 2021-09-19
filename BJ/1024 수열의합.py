def solution():
    N, L = list(map(int, input().split(" ")))

    while L < 101:

        for cur in range(101):
            start = (N // L) - cur

            if start < 0:
                continue

            if getUntilSum(start, L) == N:
                answer = []
                for num in range(start, start + L):
                    answer.append(str(num))
                return " ".join(answer)

        L += 1

    return -1


def getUntilSum(start, cnt):
    value = 0
    for num in range(start, start + cnt):
        value += num
    return value


output = solution()
print(output)
