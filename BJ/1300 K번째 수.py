N = int(input())
k = int(input())


def findLowerNumber(target):
    num = 0
    for i in range(1, N + 1):
        if target // i >= N:
            num += N
        else:
            num += target // i
    return num

answer = 0
def binary_search(start, end):
    global answer
    if start > end:
        return -1

    mid = (start + end) // 2
    num = findLowerNumber(mid)
    if num >= k:
        answer = mid
        binary_search(start, mid - 1)
    else:
        binary_search(mid + 1, end)


binary_search(0, N ** 2)
print(answer)
