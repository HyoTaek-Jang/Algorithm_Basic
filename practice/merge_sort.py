def merge_sort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    temp = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            temp.append(right.pop(0))
        else:
            temp.append(left.pop(0))

    temp += left + right
    return temp

arr = [1,5,23,3,2,0]

print(merge_sort(arr))