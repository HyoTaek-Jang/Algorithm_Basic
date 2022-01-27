def solution(participant, completion):
    dict = {}
    for i in participant:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in completion:
        dict[i] -= 1

    for i in participant:
        if dict[i] != 0:
            return i