K, N = map(int, input().split())
lans = []
for _ in range(K):
    lans.append(int(input()))

def binary_search(start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    cut = getLanCount(mid)
    if cut >= target:
        return mid
    if cut > target:
        return binary_search(mid + 1, end, target)
    else:
        return binary_search(start, mid - 1, target)


def getLanCount(mid):
    temp = 0
    for lan in lans:
        temp += lan // mid
    return temp


answer = binary_search(1, max(lans), N)
while True:
    temp = binary_search(answer+1, max(lans), N)
    if temp == -1:
        break
    answer = temp

print(answer)
