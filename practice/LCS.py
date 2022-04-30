import pprint

def lcs(a, b):
    board = [[0] * (len(b)+1) for _ in range(len(a)+1)]

    for row in range(1,len(a)+1):
        for col in range(1,len(b)+1):
            if a[row-1] == b[col-1]:
                board[row][col] = board[row-1][col-1] + 1
            else:
                board[row][col] = max(board[row-1][col], board[row][col-1])

    print(board[len(a)][len(b)])
    pprint.pprint(board)

lcs("abcqwer", "bascer")