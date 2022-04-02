arr = [1, 41, 15, 5, 2]


def bubbleSort(arr):
    length = len(arr)

    for _ in range(length):
        for start in range(length - 1):
            if arr[start] > arr[start + 1]:
                arr[start], arr[start + 1] = arr[start + 1], arr[start]

    print(arr)


# bubbleSort(arr)

def mergeSort(arr):
    length = len(arr)
    if length == 1:
        return arr

    left = mergeSort(arr[0: length // 2])
    right = mergeSort(arr[length // 2:])

    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
        print(1)
    result = result + left + right

    return result

print(mergeSort(arr))

def quick_sort(arr):
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
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)