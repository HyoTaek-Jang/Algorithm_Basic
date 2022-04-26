# 한 사이클마다, 맨 뒤의 값이 정해짐

def bubble_sort(arr):
    for i in range(len(arr)):
        for idx in range(0, len(arr) - 1 - i):
            if arr[idx] > arr[idx + 1]:
                arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


arr = [2, 4, 1, 3, 8, 6]

bubble_sort(arr)

print(arr)
