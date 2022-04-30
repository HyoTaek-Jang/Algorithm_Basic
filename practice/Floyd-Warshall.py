def floyd(table):
    for mid in range(len(table)):
        for start in range(len(table)):
            for end in range(len(table)):
                if table[start][end] > table[start][mid] + table[mid][end]:
                    table[start][end] = table[start][mid] + table[mid][end]

    return table

INF = 1e9
print(floyd([[0, 2, INF, 4], [2, 0, INF, 5], [3, INF, 0, INF], [INF, 2, 1, 0]]))
