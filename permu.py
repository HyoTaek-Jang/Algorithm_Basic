def permutation(arr, cnt):
    def step(temp, visited):
        if len(temp) == cnt:
            print(temp)
            return

        for idx in range(len(arr)):
            if not visited[idx]:
                temp.append(arr[idx])
                visited[idx] = True
                step(temp, visited)
                temp.pop()
                visited[idx] = False
    visited = [False] * len(arr)
    step([], visited)

permutation([1,2,3], 2)
