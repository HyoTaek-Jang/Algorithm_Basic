def solution(arr, target):
    arr.sort()

    front = 0
    rear = len(arr) - 1

    while front < rear:
        sum_ = arr[front] + arr[rear]
        if sum_ == target:
            return [arr[front], arr[rear]]

        if sum_ > target:
            rear -= 1
        else:
            front += 1
    return None


arr = [5, 2, 1, 5, 7, 32, 123, 67]

print(solution(arr, 12))
