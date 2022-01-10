N = int(input())

positive = []
negative = []
zero = []
for _ in range(N):
    cur = int(input())
    if cur > 0:
        positive.append(cur)
    if cur == 0:
        zero.append(cur)
    if cur < 0:
        negative.append(cur)
positive.sort(reverse=True)
negative.sort()

answer = 0
for idx in range(len(positive)//2):
    if positive[idx*2] == 1 or positive[idx*2+1] == 1:
        answer += positive[idx*2] + positive[idx*2+1]
        continue
    answer += positive[idx*2] * positive[idx*2+1]
if len(positive) % 2 != 0:
    answer += positive[len(positive)-1]

for idx in range(len(negative)//2):
    answer += negative[idx*2] * negative[idx*2+1]
if len(negative) and len(negative) % 2 != 0:
    if not len(zero):
        answer += negative[len(negative)-1]

print(answer)