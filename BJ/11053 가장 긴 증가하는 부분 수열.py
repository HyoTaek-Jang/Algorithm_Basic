N = int(input())
array = list(map(int, input().split()))

dp = [1] * len(array)

for idx in range(1, len(array)):
    for inner in range(idx):
        if array[idx] > array[inner]:
            dp[idx] = max(dp[inner] + 1, dp[idx])

print(max(dp))