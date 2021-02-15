from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while len(people):
        if people[0] + people[-1] > limit:
            people.pop()
        elif people[0] + people[-1] <= limit:
            people.pop()
            people.popleft()
        answer += 1

    return answer
