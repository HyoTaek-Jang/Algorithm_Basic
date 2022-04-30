import itertools

def permutation(target, length):
    used = [0 for _ in range(len(target))]
    target = list(set(target))

    def generate_permu(chosen, used):
        if len(chosen) == length:
            print(chosen)
            return

        for idx in range(len(target)):
            if used[idx] == 0:
                chosen.append(target[idx])
                used[idx] = 1
                generate_permu(chosen, used)
                used[idx] = 0
                chosen.pop()

    generate_permu([], used)


permutation([1, 1, 2, 3, 4], 3)
