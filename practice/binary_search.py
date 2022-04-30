# def binary_search(arr, target):
#     arr.sort()
#
#     start = 0
#     end = len(arr) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if arr[mid] == target:
#             return True
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#
#     return False

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


arr = [2, 4, 1, 6, 7, 23, 12]
arr.sort()
# print(binary_search(arr, 6))
print(arr)
print(binary_search(arr, 6, 0, len(arr) - 1))

