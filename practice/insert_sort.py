# 정렬안된 맨 뒤의 값을 앞쪽에 넣는 방식
def insertion_sort(arr):
    for outer in range(1, len(arr)):
        for inner in range(outer):
            if arr[outer] < arr[inner]:
                arr[outer], arr[inner] = arr[inner], arr[outer]


arr = [2, 4, 1, 10, 8]

insertion_sort(arr)

print(arr)
