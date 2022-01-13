import sys

N, C = map(int, sys.stdin.readline().strip().split())
locations = []
for _ in range(N):
    locations.append(int(sys.stdin.readline().strip()))
locations.sort()

answer = -1


def binary(start, end):
    global answer
    if start > end:
        return -1
    mid = (start + end) // 2
    if checkDistance(mid):
        answer = max(mid, answer)
        return binary(mid + 1, end)
    binary(start, mid - 1)


def checkDistance(distance):
    temp = -1
    temp_C = C # 공유기 개수
    for location in locations:
        if temp == -1 or location - temp >= distance:
            temp = location
            temp_C -= 1
        if temp_C == 0:
            return True
    return False


#     가장 인접한 공유기 거리를 길게!
#     정답은 가장 가까운 공유기 거리

binary(1, locations[-1])
print(answer)
