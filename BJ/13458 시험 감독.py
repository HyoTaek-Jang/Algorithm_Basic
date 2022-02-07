import sys

si = sys.stdin

N = int(si.readline())
A = list(map(int, si.readline().strip().split()))
B, C = map(int, si.readline().split())

answer = 0
for i in A:
    i -= B
    answer += 1
    if i <= 0:
        continue
    answer += (i // C)
    if i % C != 0:
        answer += 1

print(answer)