from itertools import permutations


def isPrimeNumber(num):
    if (num <= 1):
        return False
    divisor = 2
    while (divisor < int((num ** 0.5) + 1)):
        if num % divisor == 0:
            return False
        divisor += 1
    return True


def solution(numbers):
    numbers = [i for i in numbers]

    answer = 0
    perNums = []
    setNums = []

    for i in range(1, len(numbers) + 1):
        perNums.append(list(permutations(numbers, i)))

    for i in perNums:
        for j in i:
            temp = ""
            for k in j:
                temp += k
            setNums.append(int(temp))

    setNums = set(setNums)

    for i in setNums:
        if isPrimeNumber(i):
            answer += 1

    return answer