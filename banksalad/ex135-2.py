import copy


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_min_sum(root):
    min_sum = 1e9
    min_path = []

    temp = []
    temp.append([root, 0, []])
    while temp:
        root, sum, path = temp.pop()
        if root is None:
            if min_sum > sum:
                min_path = copy.deepcopy(path)
                min_sum = sum
            continue
        sum += root.value
        path.append(root.value)

        temp.append([root.left, sum, copy.deepcopy(path)])
        temp.append([root.right, sum, copy.deepcopy(path)])

    return [min_sum, min_path]


root = Node(5, Node(3, Node(6)), Node(18))
print(find_min_sum(root))
