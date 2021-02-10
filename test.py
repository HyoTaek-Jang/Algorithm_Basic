from itertools import combinations


def solution(number, k):
    length = [i for i in range(len(number))]
    _numList = []

    for i in combinations(length, len(number)-k):
        print(i)
        _numList.append(''.join(number[j] for j in i))
    _numList.sort(reverse=True)
    return _numList[0]


# 젤 큰 수가 처음 그다음이 그다음

print(solution('1234', 2))
