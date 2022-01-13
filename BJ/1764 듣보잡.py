import sys

N, M = map(int, sys.stdin.readline().strip().split())
noSound = set()
noSee = set()

for _ in range(N):
    noSound.add(sys.stdin.readline().strip())
for _ in range(M):
    noSee.add(sys.stdin.readline().strip())

answer = []
for i in noSound:
    if i in noSee:
        answer.append(i)

answer.sort()

print(len(answer))
for i in answer:
    print(i)