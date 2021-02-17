# 프로그래머스 레벨 2 구명보트

# try 1 성공
from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)

    while len(people):
        if len(people) > 1 and people[0] + people[-1] <= limit : people.popleft()
        people.pop()
        answer += 1

    return answer
