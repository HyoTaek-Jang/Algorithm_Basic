import copy
import sys

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

dp = [[0] * N for _ in range(K+1)]
for i in range(len(coins)):
    dp[coins[i]][i] = 1

for money in range(K+1):
    for coin in range(len(coins)):
        if 0 <= money - coins[coin]:
            temp = copy.deepcopy(dp[money - coins[coin]])
            temp[coin] += 1
            if sum(dp[money]) == 0:
                dp[money] = temp
            else:
                if sum(dp[money]) > sum(temp):
                    dp[money] = temp


print(dp[K])
5
11111
2111
221

11111 111111
11111 1112
11111 122
11111 5
1112 5
1112 122
1112 1112
122 122
5 5
22222