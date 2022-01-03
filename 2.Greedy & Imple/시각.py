def solution():
    N = int(input())

    answer = 0
    for hours in range(N+1):
        for minutes in range(60):
            for seconds in range(60):
                if '3' in str(hours) or '3' in str(minutes) or '3' in str(seconds):
                # if '3' in str(i) + str(j) + str(k):
                    answer += 1

    print(answer)

solution()