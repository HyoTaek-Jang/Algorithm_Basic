def solution(triangle):
    length = len(triangle)
    dp = [[0] * length for _ in range(length)]
    dp[0][0] = triangle[0][0]

    for row in range(1, length):
        for col in range(len(triangle[row])):
            if 0 <= col - 1:
                dp[row][col] = max(dp[row - 1][col - 1] + triangle[row][col], dp[row][col])
            if col < len(triangle[row - 1]):
                dp[row][col] = max(dp[row - 1][col] + triangle[row][col], dp[row][col])

    return max(dp[length - 1])