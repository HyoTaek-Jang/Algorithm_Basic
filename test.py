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


print(subset_sum([2, 3, 20, 27, 8], 0, 0, 60, 13, [0, 0, 0, 0, 0]))
