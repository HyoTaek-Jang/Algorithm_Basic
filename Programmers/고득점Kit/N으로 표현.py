def solution(N, number):
    dp = [set()]
    for cnt in range(1, 9):
        dp.append(set())
        dp[cnt].add(int(str(N) * cnt))

        left = 1
        right = cnt - 1
        print(len(dp), cnt)
        while left <= right:
            for right in dp[right]:
                for left in dp[left]:
                    dp[cnt].add(right + left)
                    dp[cnt].add(right // left)
                    dp[cnt].add(right * left)
                    dp[cnt].add(right - left)
            left += 1
            right -= 1

        if number in dp[cnt]:
            return cnt

    return -1

solution(8,53)