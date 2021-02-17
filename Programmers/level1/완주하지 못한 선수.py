#
'''
def solution(participant, completion):
    i=0
    while len(completion):
        if participant[i] in completion:
            completion.remove(participant[i])
        else:
            return participant[i]
        i+=1
    return participant[0]
'''

''' 차집합 실패
def solution(participant, completion):
    p = set(participant)
    c = set(completion)
    p-c
'''


def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]
