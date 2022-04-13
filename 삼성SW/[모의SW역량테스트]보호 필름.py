# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

import sys

'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
import copy

sys.stdin = open("input.txt", "r")

T = int(input())


def is_success_table(table, K):
    for col in range(len(table[0])):
        max_connect = 1
        prev = table[0][col]
        fail = True
        for row in range(1, len(table)):
            if max_connect >= K:
                fail = False
                break
            if table[row][col] == prev:
                max_connect += 1
            else:
                prev = table[row][col]
                max_connect = 1
        if fail and max_connect < K:
            return False
    return True


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def combination(result, arr, temp, k):
    if len(temp) == k:
        result.append(copy.deepcopy(temp))
        return result

    if temp:
        start = arr.index(temp[-1]) + 1
    else:
        start = 0
    for idx in range(start, len(arr)):
        temp.append(arr[idx])
        combination(result, arr, temp, k)
        temp.pop()

    return result


def dfs(table, case, current_idx, K):
    if current_idx == len(case):
        return is_success_table(table, K)

    for attr in [0, 1]:
        table[case[current_idx]] = [attr] * W
        result = dfs(table, case, current_idx + 1, K)
        if result:
            return True
    return False


for test_case in range(1, T + 1):
    D, W, K = map(int, input().strip().split())
    table = [list(map(int, input().strip().split())) for _ in range(D)]

    if is_success_table(table, K):
        print("#" + str(test_case) + " " + str(0))
        continue

    start = 1
    end = D
    choice = [i for i in range(D)]
    temp = -1
    while start <= end:
        mid = (start + end) // 2
        cases = combination([], choice, [], mid)
        flag = True
        for case in cases:
            temp_table = copy.deepcopy(table)
            if dfs(temp_table, case, 0, K):
                temp = mid
                end = mid - 1
                flag = False
                break
        if flag:
            start = mid + 1
    print("#" + str(test_case) + " " + str(temp))
