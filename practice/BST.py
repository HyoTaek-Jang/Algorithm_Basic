# bst
# append, 특정 값 찾기

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.value} [left : {self.left}, right : {self.right}]'


class BST:
    def __init__(self, node):
        self.root = node

    def append(self, node):
        current = self.root

        while True:
            if current.value > node.value:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right

    def __str__(self):
        return f'{self.root}'


def is_bst(node):
    if node.left is None and node.right is None:
        return True

    left = node.left
    right = node.right
    left_result = True
    right_result = True

    if left is not None:
        if node.value <= left.value:
            return False
        left_result = is_bst(left)

    if right is not None:
        if node.value >= right.value:
            return False
        right_result = is_bst(right)

    return left_result and right_result


bst = BST(Node(5))
bst.append(Node(3))
bst.append(Node(4))

print(is_bst(bst.root))
