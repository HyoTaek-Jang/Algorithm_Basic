class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f'<value : {self.value}, left : {self.left}, right : {self.right}>'

class BinarySearchTree:
    def __init__(self, node):
        self.root = node

    def __str__(self):
        return f'{self.root}'

    def add(self, node):
        current = self.root

        while True:
            if node.value > current.value:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
            else:
                if current.left is None:
                    current.left = node
                    break
                current = current.left

bst = BinarySearchTree(Node(5))
bst.add(Node(2))
bst.add(Node(3))
print(bst)