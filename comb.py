def combination(arr, cnt):
    arr = list(set(arr))

    def step(temp):
        if len(temp) == cnt:
            print(temp)
            return

        last_idx = arr.index(temp[-1]) + 1 if len(temp) != 0 else 0

        for idx in range(last_idx, len(arr)):
            temp.append(arr[idx])
            step(temp)
            temp.pop()

    step([])


combination([1,2,5,6], 2)