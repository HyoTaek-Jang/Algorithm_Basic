import bisect

N, x = map(int, input().split())
array = list(map(int, input().split()))

left = bisect.bisect_left(array, x)
right = bisect.bisect_right(array, x)

print(right-left)