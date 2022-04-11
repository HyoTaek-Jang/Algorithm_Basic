def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return None


print(binary_search([1, 2, 3, 7, 8, 13], 9))
