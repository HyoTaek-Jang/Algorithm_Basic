import sys

N = int(sys.stdin.readline())

schedule = []
for _ in range(N):
    schedule.append(list(map(int, sys.stdin.readline().strip().split())))

dp = [0] * N

for idx in range(len(schedule)):
    dp[idx] = dp[idx-1]
    for end in range(idx+1):
        cur = schedule[end]
        end_date = cur[0] + end - 1
        if end_date == idx and dp[idx] < dp[idx-cur[0]] + cur[1]:
            dp[idx] = dp[idx-cur[0]] + cur[1]

print(max(dp))
