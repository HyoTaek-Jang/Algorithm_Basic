def subset_sum(A, s, k, r, B, w):
    w[k] = 1
    a = False
    if s + A[k] == B:
        return True
    elif s + A[k] <= B:
        a = subset_sum(A, s + A[k], k + 1, r - A[k], B, w)
    if not a and s + r - A[k] >= B:
        w[k] = 0
        a = subset_sum(A, s, k + 1, r - A[k], B, w)
    return a


# print(subset_sum([2, 3, 20, 27, 8], 0, 0, 60, 13, [0, 0, 0, 0, 0]))


def subset_sum_dp(A, target):
    A.sort()

    target += 1

    _dp = [[False] * target for i in range(len(A))]

    for i in range(target):
        if i == A[0]:
            _dp[0][i] = True

    for i in range(1, len(A)):
        for j in range(target):
            if j == A[i]:
                _dp[i][j] = True
            elif _dp[i - 1][j]:
                _dp[i][j] = True
            elif j - A[i] >= 0and _dp[i - 1][j - A[i]]:
                _dp[i][j] = True

    target -= 1
    for i in range(len(A)):
        if _dp[i][target]:
            return True

    return False


print(subset_sum_dp([2, 3, 20, 27, 8],13))
