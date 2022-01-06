N = int(input())

left_upper = [False] * (2 * N)
right_upper = [False] * (2 * N)
center = [False] * N


def dfs(row, answer):
    for col in range(N):
        if row == N:
            return answer
        if center[col] or right_upper[col + row] or left_upper[row - col + N - 1]:
            continue
        if row == N - 1:
            answer += 1
        center[col] = right_upper[row + col] = left_upper[row - col + N - 1] = True
        answer = dfs(row + 1, answer)
        center[col] = right_upper[row + col] = left_upper[row - col + N - 1] = False

    return answer


print(dfs(0, 0))
