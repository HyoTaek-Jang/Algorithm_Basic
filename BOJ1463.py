# 1차 알고리즘 짜려다 실패
# 2차 재귀로 모든 경우 계산, 리컬젼 에러
# 3차 덱으로 와일 -> 메모리초과
# 아웅...
# 4차 1 연속으로 두번 더하면 패스, num보다 큰 값은 배열에 안넣음 -> 메모리 초과
# 5차 count의 min보다 큰놈은 패스 - > 시간초과
# 6차 min-2보다 큰애도 패스
# 성공

# 근데 DP로 푸는거래..ㅎ

# 백준 1463번 1로 만들기

from collections import deque


def makeByOne():
    num = int(input())
    count = []
    calNum = deque([(num, 0, 0)])
    while calNum:
        cur = calNum.popleft()
        if cur[2] >= 3:
            continue
        elif cur[0] == 1:
            count.append(cur[1])
        elif len(count) > 0 and cur[1] > min(count)-2:
            continue
        if cur[0] % 3 == 0 and (cur[0] // 3 == 1 or cur[0] // 3 >= 3):
            calNum.append((cur[0] // 3, cur[1] + 1, 0))
        if cur[0] % 2 == 0 and (cur[0] // 2 == 1 or cur[0] // 2 >= 2):
            calNum.append((cur[0] // 2, cur[1] + 1, 0))
        if cur[0] - 1 >= 1:
            calNum.append((cur[0] - 1, cur[1] + 1, cur[2] + 1))

    print(min(count))


makeByOne()

#
# def cal(num, target, curCount, count):
#     if num > target:
#         return
#     elif num == target:
#         return count.append(curCount)
#     curCount += 1
#     cal(num * 3, target, curCount, count)
#     cal(num * 2, target, curCount, count)
#     cal(num + 1, target, curCount, count)
#

# L = set([int(input())])
# N = 0
#
# while True:
#     if 1 in L:
#         break
#     M = set()
#     for i in L:
#         if i%3 == 0:
#             M.add(i/3)
#         if i%2 == 0:
#             M.add(i/2)
#         M.add(i-1)
#     N += 1
#     L = M.copy()
# print(N)