def combination(arr, length):
    arr.sort()
    arr = list(set(arr))

    def generate(chosen):
        if len(chosen) == length:
            print(chosen)
            return

        start = arr.index(chosen[-1]) + 1 if chosen else 0

        for idx in range(start, len(arr)):
            chosen.append(arr[idx])
            generate(chosen)
            chosen.pop()

    generate([])

combination([1,2,3],2)

