N = int(input())
array = list(map(int,input().split()))

array.sort()

answer = 0

length = len(array)
for idx in range(length):
    answer += array[idx] * (length - idx)

print(answer)