N = int(input())
soldier = list(map(int, input().split()))
soldier.reverse()
distance = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if soldier[i] > soldier[j]:
            distance[i] = max(distance[i], distance[j] + 1)

print(N - max(distance))
