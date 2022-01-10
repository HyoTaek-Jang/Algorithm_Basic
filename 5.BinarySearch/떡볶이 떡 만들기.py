N, M = map(int, input().split())
cakes = list(map(int, input().split()))
cakes.sort()
answer = -1

def binary_serch(start, end, target):
    global answer

    if start > end:
        return None
    mid = (start + end) // 2
    customer = getCakes(mid)
    if target <= customer:
        answer = max(mid, answer)
    if target == customer:
        return mid
    elif target > customer:
        return binary_serch(start, mid - 1, target)
    else:
        return binary_serch(mid + 1, end, target)


def getCakes(target):
    value = 0
    for idx in range(len(cakes) - 1, -1, -1):
        if cakes[idx] < target:
            return value
        value += cakes[idx] - target
    return value


binary_serch(0, max(cakes), M)
print(answer)