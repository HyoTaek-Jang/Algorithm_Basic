A = list(input())
B = list(input())

length = len(A)
lengthB = len(B)

dp = [[0] * lengthB for _ in range(length)]

for row in range(length):
    for col in range(lengthB):
        if A[row] == B[col]:
            if 0 <= row - 1 and 0 <= col - 1:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                dp[row][col] = 1
        else:
            if 0 <= row - 1:
                dp[row][col] = max(dp[row][col], dp[row - 1][col])
            if 0 <= col - 1:
                dp[row][col] = max(dp[row][col], dp[row][col - 1])

print(dp[length - 1][lengthB - 1])
