N, M = map(int, input().split())

answer = []
history = set()


def dfs():
    for i in range(1, N + 1):
        if len(answer) == M:
            # if ''.join(map(str, answer)) in history:
            #     return
            print(' '.join(map(str, answer)))
            return
            # history.add(''.join(map(str, answer)))
        # if len(answer) > M:
        #     return
        answer.append(i)
        dfs()
        answer.pop()


dfs()
