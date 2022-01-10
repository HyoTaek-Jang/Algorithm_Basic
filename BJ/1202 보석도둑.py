import heapq
import sys


N, K = map(int, sys.stdin.readline().split())

treasure = []  # 무게, 가격
for _ in range(N):
    weight, price = map(int, sys.stdin.readline().split())
    heapq.heappush(treasure, (weight, price))

bags = []
for _ in range(K):
    heapq.heappush(bags, int(sys.stdin.readline()))


filtered = []
answer = 0

for _ in range(K):
    bag = heapq.heappop(bags)
    while len(treasure) and bag >= treasure[0][0]:
        heapq.heappush(filtered, -heapq.heappop(treasure)[1])
    if not len(filtered):
        continue
    answer += -heapq.heappop(filtered)

print(answer)
