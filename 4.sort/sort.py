'''
정렬 알고리즘 : 특정한 기준에 따라 순서대로 나열 하는 것
문제 상황에 따라 적절한 정렬 알고리즘이 공식처럼 사용함.
'''

'''
선택정렬
: 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복. 마지막 경우는 처리 안해도 된당!
O(N^2)
'''

'''
삽입정렬
: 데이터를 하나씩 골라 적절한 위치에 삽입한다.
구현 난이도는 높으나 더 효율적임

첫 번째 데이터는 그 자체로 정렬 됐다고 판단. 두 번째부터 정렬 실행. 정렬된 애들 중에서 어디에 들어가야하나 체크함. 

얘도 O(N^2)d임.
근데 만약 현재 리스트가 정렬되어있으면 매우 빠름
최선의 경우 O(N)임.ㅠ 
'''


def sort_insert():
    array = [1, 6, 5, 4, 7, 3, 2, 1, 0]
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break
    print(array)


sort_insert()

'''
퀵정렬
빠른 정렬 알고리즘
일반적으로 데이터 특성과 상관없이 사용가능
기준 데이터를 고르고 기준보다 크고 작은 데이터의 위치를 바꾸는 방법
가장 많이 사용
가장 기본적인 퀵 정렬은 첫 번째 데이터를 기준 데이터(pivot)으로 설정함. 
그 다음 왼쪽에서부터 피벗보다 큰 값을 고르고 오른쪽에서부터 피벗보다 작은 값을 고르고 서로 바꿈. 만약 근데 쭉쭉 가다가 작은게 왼쪽에 있으면
피벗이랑 작은거랑 바꿈
그리고 피벗을 중심으로 양쪽을 나누고 양쪽에 다시 퀵소트 실행

이상적으로  분할이 절반씩 일어나면 NlogN
최악의 경우 N^2
평균은 NlogN
정렬된 놈에게 퀵소트하면 최악... 
근데 라이브러리는 최소 NlogN을 보장함 
'''


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    left = [i for i in tail if pivot >= i]
    right = [i for i in tail if pivot < i]
    return quick_sort(left) + [pivot] + quick_sort(right)


a = quick_sort([1, 0, 3, 2, 6, 5, 8, 5, 7])
print(a)

'''
계수 정렬
특정한 조건에서만 사용가능 매우 빠름
    데이터의 크기 범위가 제한되어 정수 형태로 표현 할 수 있을 때 사용가능
 데이터가 N개, 최대값이 K일때 최악의 경우에도 O(N+K)를 보장
 
 데이터를 확인하면서 몇번 등장했는지 카운트를 체크함.
 그리고 카운트랑 인덱스를 확인하면서 출력함.
 
 O(N+K)
 
동일한 값이 여러 개 등장할때 효과점. 
성적같은 경우 효과적이당

퀵이랑 계수가 젤 난듯
'''


# 문제> 두 배열의 원소 교체
def change():
    N, K = map(int, input().split(' '))
    arrayA = list(map(int, input().split(' ')))
    arrayB = list(map(int, input().split(' ')))

    for i in range(K):
        maxIndexB = arrayB.index(max(arrayB))
        minIndexA = arrayA.index(min(arrayA))
        arrayA[minIndexA], arrayB[maxIndexB] = arrayB[maxIndexB], arrayA[
            minIndexA]
    print(sum(arrayA))


# change()

# 백준 11728번 배열 합치기
def combine():
    M, N = input().split(' ')
    listA = list(map(int, input().split(' ')))
    listB = list(map(int, input().split(' ')))
    result = listA + listB
    result.sort()
    for i in result:
        print(i, end=' ')


# combine()

# 신입 사원 1946번
def recruit():
    case = int(input())
    countList = []
    for _ in range(case):
        M = int(input())
        count = 0
        xlist = []
        ylist = []

        for i in range(M):
            x, y = (map(int, input().split()))
            xlist.append((i,x,y))
            ylist.append(y)

        xlist.sort(reverse=True, key=lambda x: x[1])
        ylist.sort()
        length = len(xlist)

        for i in range(length):
            if xlist[i][2] == ylist[0]:
                count += 1
            ylist.remove(xlist[i][2])

        countList.append(count)
    for i in countList:
        print(i)

recruit()
