V = int(input())
dict = {}
for _ in range(V):
    current = list(map(int, input().split()))
    dict[current[0]] = {}
    for i in range(1, len(current) // 2):
        dict[current[0]][current[i * 2 - 1]] = current[i * 2]

answer = -1

leaf = []


def dfs(start, length, visited):
    new_length = -1
    visited[start] = False
    for j in dict[start]:
        if visited[j]:
            length += dict[start][j]
            visited[j] = False
            new_length = max(dfs(j, length, visited), new_length)
            visited[j] = True
            length -= dict[start][j]
    if new_length == -1:  # 리프 노드
        leaf.append([length, start])
    return max(length, new_length)


dfs(1, 0, [True] * (V + 1))
leaf.sort(reverse=True)
answer = dfs(leaf[0][1], 0, [True] * (V + 1))

print(answer)

# https://blog.myungwoo.kr/112