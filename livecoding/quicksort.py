from functools import cmp_to_key

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[pivot] >= arr[left]:
            left += 1
        while right > start and arr[pivot] <= arr[right]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

        quick_sort(arr, start, right - 1)
        quick_sort(arr, right + 1, end)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort2(lesser_arr) + equal_arr + quick_sort2(greater_arr)

arr = [2,3,1,4,5]

# quick_sort(arr, 0, len(arr)-1)
arr = quick_sort2(arr)
print(arr)