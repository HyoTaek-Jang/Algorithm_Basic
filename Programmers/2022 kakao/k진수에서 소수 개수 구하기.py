def solution(n, k):
    num = str(makeNumber(n, k))
    targets = num.split('0')

    answer = 0
    for i in targets:
        if i.isdigit() and isPrime(int(i)):
            answer += 1

    return answer


def isPrime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** (0.5) + 1)):
        if n % i == 0 and i != n:
            return False
    return True


def makeNumber(n, k):
    temp = []
    while n > 0:
        rest = n % k
        value = n // k
        n = value
        temp.append(str(rest))
    temp.reverse()
    return "".join(temp)