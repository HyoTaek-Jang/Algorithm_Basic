cycle = int(input())
count = 0


for i in range (cycle):
    a, b = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort()

    for k in range(a):
        for j in range(b):
            if A[k] > B[j]:
                count = count + 1

    print(count)