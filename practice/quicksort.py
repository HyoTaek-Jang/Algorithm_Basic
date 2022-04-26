def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    left, mid, right = [], [], []

    pivot = arr[0]
    for current in arr:
        if current > pivot:
            right.append(current)
        elif current == pivot:
            mid.append(current)
        else:
            left.append(current)

    return quick_sort(left) + mid + quick_sort(right)


def quick_sort2(arr, start, end):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left < right:
        # left가 pivot보다 큰 값을 찾을 때까지
        while left <= end and arr[left] < arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quick_sort2(arr, start, right - 1)
    quick_sort2(arr, right + 1, end)


arr = [2, 3, 1, 4, 5]
# print(quick_sort(arr))
quick_sort2(arr, 0, len(arr)-1)
print(arr)