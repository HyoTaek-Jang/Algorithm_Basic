# def select_sort(arr):
#     for end in range(len(arr), 0, -1):
#         max_value = arr[0]
#         max_idx = 0
#         for idx in range(1, end):
#             if max_value < arr[idx]:
#                 max_idx = idx
#                 max_value = arr[idx]
#         arr[end - 1], arr[max_idx] = max_value, arr[end - 1]

# 젤 작은 값이나 젤 큰 값을 구해서, 앞이나 뒤에 옮겨둠

def select_sort(arr):
    for start in range(len(arr) - 1):
        min_idx = start
        for idx in range(start, len(arr)):
            if arr[min_idx] > arr[idx]:
                min_idx = idx
        arr[start], arr[min_idx] = arr[min_idx], arr[start]


arr = [2, 1, 4, 5, 8, 7]
select_sort(arr)
print(arr)
