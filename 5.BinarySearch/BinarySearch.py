'''
순차 탐색 : 특정 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 확인 하는것 시간복잡도 N
이진 탐색 : 탐색 범위를 절반씩 좁히며 데이터를 탐색함. 정렬이 되어있을때! 시간복잡도 log
시작점, 끝점, 중간점을 활용함. 중간점은 반으로 쪼개고 소수점을 날림.
그리고 비교해서 시작, 중간, 끝을 다시 정해서 반복
'''
import sys
import bisect

'''
이진탐색 라이브러리
bisect_left(a, x) : 정렬을 유지하면서 x가 삽입될 가장 왼쪽 인덱스를 반환
bisect_right(a, x) : 오른쪽

두개를 활용해서 범위안에 데이터 몇개인지 확인 가능
'''

'''
파라메트릭 서치
: 최적화 문제를 결정문제로 바꾸어 해결하는 기법
최적화 문제 : 어떤 함수 값을 가능한 낮추거나 최대한 높이는 문제
'''


# 떡볶이 떡 만들기
# 1차 실패
# 
# def riceCake():
#     M, N = map(int, sys.stdin.readline().split(' '))
#     cakes = list(map(int, sys.stdin.readline().split(' ')))
#     cakes.sort()
# 
#     minValue = 0
#     maxValue = M
#     cul = (cakes[minValue] + cakes[maxValue-1]) // 2
# 
#     culCheck = True
#     check = True
# 
#     count = cut(cakes, cul, minValue, maxValue)
# 
#     if count == N:
#         return print(cul )
#     elif count > N:
#         cul += 1
#         minValue = bisect_right(cakes, cul)
#         check = False
#     else:
#         cul -= 1
#         maxValue = bisect_right(cakes, cul)
#         culCheck = False
# 
#     while culCheck == True and check == True: 
#         count = cut(cakes, cul, minValue, maxValue)
# 
#         if count == N:
#             print(cul)
#             break
#         elif count > N:
#             cul += 1
#             minValue = bisect_right(cakes, cul)
#             culCheck = True
#         else:
#             cul -= 1
#             maxValue = bisect_right(cakes, cul)
#             check = True
# 
#     print(cul)
# 
# 
# def cut(cakes, cul, minIdx, maxIdx):
#     count = 0
#     for i in range(minIdx, maxIdx):
#         count += cakes[i] - cul
# 
#     return count
# 
# 
# riceCake()

# 특정 수의 개수 구하기
def getCount():
    M, N = map(int, sys.stdin.readline().split(' '))
    num = list(map(int, sys.stdin.readline().split(' ')))

    left = bisect.bisect_left(num, N)
    right = bisect.bisect_right(num, N)
    count = right - left

    # count = num.count(N)
    if count == 0:
        return print(-1)
    print(count)


# getCount()

def binarySearh(numList, target):
    min = 0
    max = len(numList) - 1

    while min <= max:
        mid = (min + max) // 2
        if numList[mid] > target:
            max = mid - 1
        elif numList[mid] == target:
            return mid
        else:
            min = mid + 1
    return -1


# print(binarySearh([1, 5, 7, 8, 9, 13, 67], 1))

# 백준 1365번 꼬인 전깃줄 ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ1등ㅋㅋㅋㅋㅋㅋㅋㅋㅋ

def electronic():
    M = int(sys.stdin.readline())
    sticks = list(map(int, sys.stdin.readline().split()))

    dp = []
    dp.append(sticks[0])

    for i in range(1, len(sticks)):
        if sticks[i] > dp[-1]:
            dp.append(sticks[i])
        else:
            idx = bisect.bisect_left(dp, sticks[i])
            dp[idx] = sticks[i]

    print(M-len(dp))


# electronic()


# 백준 7795번 먹을 것인가 먹힐 것인가 오!!!!!!!대박 나 2등ㅋㅋㅋ
'''
M이랑 N 소트하고
N 인덱스에 따라서 M의 갯수를 정하는?
N소트하고 M 값마다 bisect?
'''

def eat():
    testCase = int(sys.stdin.readline())

    for _ in range(testCase):
        M, N = (map(int, sys.stdin.readline().split()))
        listA = list(map(int, sys.stdin.readline().split()))
        listB = list(map(int, sys.stdin.readline().split()))

        listB.sort()
        result = 0

        for i in listA:
            result += bisect.bisect_left(listB, i)

        print(result)


# eat()
