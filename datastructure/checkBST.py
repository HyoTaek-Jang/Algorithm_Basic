class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def isBST(root, upper_bound_exist, lower_bound_exist, upper_bound, lower_bound):
    if root is None:
        return True

    if upper_bound_exist and root.value >= upper_bound:
        return False
    if lower_bound_exist and root.value <= lower_bound:
        return False

    return isBST(root.left, True, lower_bound_exist, root.value, lower_bound) and isBST(root.right, upper_bound_exist,
                                                                                        True, upper_bound,
                                                                                        root.value)


bst = Node(4, Node(2), Node(6, None, Node(5)))
print(isBST(bst, False, False, 0, 0))
