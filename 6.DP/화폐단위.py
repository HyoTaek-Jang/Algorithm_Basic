N, M = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))

money_dp = [1e9] * (M+1)

for cur in money:
    if cur < M:
        money_dp[cur] = 1

for i in range(1,M+1):
    for cur in money:
        if i-cur > 1 and money_dp[i-cur] != 1e9:
            money_dp[i] = min(money_dp[i-cur]+1, money_dp[i])

if money_dp[M] == 1e9:
    print(-1)
else:
    print(money_dp[M])
