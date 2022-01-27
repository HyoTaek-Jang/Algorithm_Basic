def solution(clothes):
    dict = {}

    keys = 0
    for cur in clothes:
        if cur[1] in dict:
            dict[cur[1]] += 1
        else:
            dict[cur[1]] = 1
            keys += 1

    answer = 1
    for i in dict:
        answer *= (dict[i] + 1)

    return answer - 1