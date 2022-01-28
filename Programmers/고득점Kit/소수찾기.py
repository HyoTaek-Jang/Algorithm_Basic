import itertools


def solution(numbers):
    result = set([])
    for n in range(1, len(numbers) + 1):
        a = list(itertools.permutations(numbers, n))
        for i in a:
            result.add(int("".join(i)))

    answer = 0
    for cur in result:
        check = True
        if cur == 0 or cur == 1:
            continue
        for div in range(2, int(cur ** (0.5)) + 1):
            if cur % div == 0:
                check = False
                break
        if check:
            answer += 1

    return answer