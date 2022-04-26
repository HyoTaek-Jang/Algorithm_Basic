# 주어진 배열 arr에 n개의 정수 타입 숫자들이 정렬 되어 들어가 있다. 여기서 임의의 숫자 target가 그 배열의 몇 번 째에 있는지 반환하는 함수를 구현하라.
# arr = [1, 2, 9, 78, 124]
# arr = [1, 99, 3, 78, 124]
# target = 9
# the return value should be 2

# def binary_search(arr, target):
#     start, end = 0, len(arr) - 1

#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return None

def binary_search(arr, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search(arr, target, start, end)


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    new_sorted = []
    while len(sorted_left) and len(sorted_right):
        if sorted_left[0] > sorted_right[0]:
            value = sorted_right.pop(0)
        else:
            value = sorted_left.pop(0)
        new_sorted.append(value)

    new_sorted += sorted_left + sorted_right

    return new_sorted


# print(merge_sort([1, 4, 3, 7, 11, 9]))


arr = [1, 2, 9, 78, 124]


# print(binary_search(arr, 9, 0, len(arr)-1))
# print(binary_search(arr, 8, 0, len(arr)-1))

# input: 인자, 기대 output
# output: 통과여부

class BinarySearchInput:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        self.start = 0
        self.end = len(self.arr) - 1


def binary_search_assert_function(parameter, expected):
    output = binary_search(parameter.arr, parameter.target, parameter.start, parameter.end)
    return output == expected


# parameter = BinarySearchInput([1, 2, 9, 78, 124], 2)
# print(binary_search_assert_function(parameter, 1))
# print(binary_search_assert_function(parameter, None))

class Assert:
    def __init__(self, func):
        self.func = func

    def assert_function(self, expected, *args):
        return self.func(*args) == expected


test = Assert(binary_search)
print(test.assert_function(2, arr, 9, 0, len(arr)-1))
