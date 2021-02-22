'''

메모리를 적절히 사용하여 수행 시간 효율성을 향상시키는 방법
이미 계산된 결과는 별도의 메모리 영역에 저장하여 다시 계산 안함.
탑다운(하향식) 방식과 바텀업(상향식) 방식이 있음

자료구조에서 동적할당이랑 동적이 같은 뜻이 아님. 동적할당은 프로그램 실행되는 중에서 실행에 필요한 메모리를 할당하는 기법

다음 조건을 만족할 시 사용 가능
1. 최적 부분 구조
    - 큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결함
2. 중복되는 부분 문제
    - 동일한 작은 문제를 반복적으로 해결해야 함

대표적인 예
    - 피보나치 수열
    - 각 항이 인접한 항과 관계식으로 표현되는 경우 점화식으로 수학적으로 명시할 수 있음.

프로그래밍에서 수열을 배열이나 리스트에 이용해 표현함.

탑다운 하향식, 메모이제이션
- 한번 계산한 결과를 메모리 공간에 메모하는 기법
- 같은 문제를 호출하면 메모한 결과를 그대로 가져옴.
- 캐싱같음.

탑다운 : 큰 문제를 해결하기 위해 작은 문제를 재귀적으로 호춯하여 모두 해결되면 자연스래 큰 문제의 답을 알게됨. 그 과정에서 한 번 계산된 값을 기록하기 위해 메모이제이션을 사용

바텀업: 아래에서 작은 문제를 해결하며 먼저 계싼한 값을 활용하며 다음 계산도 함. 반복문 사용.

DP의 전형적인 형태는 바텀업 방식
    -  결과 저장용 리스트는 DP 테이블 이라고 부른다.

메모이제이션은 이전에 계산된 값을 일시적으로 기록하는 넓은 개념이지 DP에 국한된게 아님
DP를 위해 활용하지 않을 수도 있음.

둘이 다른 개념임. 하향식을 사용할때 메모이제이션을 쓸 수 있는 거임


'''
import sys

d = [0] * 100


def TopDownfibo(x):
    if x == 1 or x == 2:
        return 1

    if d[x] != 0:
        return d[x]

    d[x] = TopDownfibo(x - 1) + TopDownfibo(x - 2)

    return d[x]


def bottomUpfibo(x):
    d = [0] * 100

    d[1] = 1
    d[2] = 2

    for i in range(3, x + 1):
        d[i] = d[i - 1] + d[i - 2]

    return d[x]


# 나동빈 개미전사
def antman():
    d = [0] * 100
    N = int(sys.stdin.readline())
    K = list(map(int, sys.stdin.readline().split(' ')))

    d[0] = K[0]

    if (K[0] < K[1]):
        d[1] = K[1]
    else:
        d[1] = d[0]

    for i in range(2, N):
        if d[i - 1] < d[i - 2] + K[i]:
            d[i] = d[i - 2] + K[i]
        else:
            d[i] = d[i - 1]

    return d[N - 1]


# print(antman())

# 나동빈 1로 만들기
def makeOne(x):
    select = []
    if x % 5 == 0 and d[x // 5] == 0:
        makeOne(x // 5)
    if x % 5 == 0 and d[x // 5] != 0:
        select.append(d[x // 5])

    if x % 3 == 0 and d[x // 3] == 0:
        makeOne(x // 3)
    if x % 3 == 0 and d[x // 3] != 0:
        select.append(d[x // 3])

    if x % 2 == 0 and d[x // 2] == 0:
        makeOne(x // 2)
    if x % 2 == 0 and d[x // 2] != 0:
        select.append(d[x // 2])

    if x - 1 > 0 and d[x - 1] == 0:
        makeOne(x - 1)
    if x - 1 > 0 and d[x - 1] != 0:
        select.append(d[x - 1])

    d[x] = min(select) + 1

    return d[x]


# N = int(sys.stdin.readline())
# d = [0] * (N + 1)
# d[0] = 999999
# d[1] = 0
# d[2] = 1
# d[3] = 1
# d[4] = 2
# d[5] = 1
#
# print(makeOne(N))

# 나동빈 화폐
def money():
    K = list(map(int, sys.stdin.readline().split(' ')))
    unit = []

    for _ in range(K[0]):
        unit.append(int(sys.stdin.readline()))

    memo = [0] * (K[1] + 1)

    for i in range(1, K[1] + 1):
        for j in unit:
            if i - j == 0:
                memo[i] = 1
            elif i - j >= 0 and memo[i - j] != -1:
                memo[i] = min(memo[i - j] + 1, memo[i]) if memo[i] != 0 else \
                    memo[i - j] + 1

        if memo[i] == 0:
            memo[i] = -1

    return memo[K[1]]


# print(money())

# 나동빈 금광
def gold():
    M = int(sys.stdin.readline())

    for _ in range(M):
        row, col = map(int, sys.stdin.readline().split(' '))
        gold = list(map(int, sys.stdin.readline().split(' ')))
        goldMap = []

        for i in range(0, len(gold), col):
            goldMap.append(gold[i:i + col])

        dp = [[0 for _ in range(col)] for _ in range(row)]

        move = [0, -1, 1]

        for i in range(row):
            dp[i][0] = goldMap[i][0]

        for i in range(1, col):
            for j in range(row):
                temp = []
                for k in move:
                    if 0 <= (j + k) < row:
                        temp.append(dp[j + k][i - 1])
                dp[j][i] = max(temp) + goldMap[j][i]

        result = []
        for i in range(row):
            result.append(dp[i][col - 1])

        return max(result)


# print(gold())


# 나동빈 병사 배치하기 백준 18353번
def soldier():
    N = int(sys.stdin.readline())
    army = list(map(int, sys.stdin.readline().split(' ')))

    dp = [1] * N

    army.reverse()

    for i in range(1, N):
        for j in range(0, i):
            if army[i] > army[j]:
                dp[i] = dp[j] + 1 if dp[j] + 1 >= dp[i] else dp[i]

    return N-max(dp)

print(soldier())