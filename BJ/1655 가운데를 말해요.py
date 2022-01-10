import sys
import heapq

N = int(sys.stdin.readline())

left = []
right = []
mid = []
size = 0
for _ in range(N):
    value = int(sys.stdin.readline())
    size += 1
    mid_length = len(mid)
    if not mid_length:
        heapq.heappush(mid, value)
    elif mid_length == 2:
        heapq.heappush(mid, value)
        heapq.heappush(left, -heapq.heappop(mid))
        temp = heapq.heappop(mid)
        heapq.heappush(right, heapq.heappop(mid))
        heapq.heappush(mid, temp)
    else:
        if size == 2 or -left[0] <= value <= right[0]:
            heapq.heappush(mid, value)
        elif -left[0] < value:
            heapq.heappush(mid, -heapq.heappop(left))
            heapq.heappush(left, -value)
        else:
            heapq.heappush(mid, heapq.heappop(right))
            heapq.heappush(right, value)

    if len(mid) == 2:
        fir = heapq.heappop(mid)
        sec = heapq.heappop(mid)
        print(min(fir, sec))
        heapq.heappush(mid, fir)
        heapq.heappush(mid, sec)
    else:
        print(mid[0])
