import sys
input = sys.stdin.readline

def sol(x, y, d, a):

    alpha = a[:]
    alpha[ord(str(m[x][y])) - 65] = 1

    result = 0

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx >= r or nx < 0 or ny >= c or ny < 0 or alpha[ord(str(m[nx][ny])) - 65]:
            continue

        result = max(result, sol(nx, ny, d+1, alpha))

    if not result:
        return d

    return result



r, c = map(int, input().split())
m = [list(input().rstrip()) for _ in range(r)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
print(sol(0, 0, 1, [0]*26))


