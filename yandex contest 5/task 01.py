class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):
        if value == self.data:
            return
        elif value < self.data:
            if self.left:
                self.left.add(value)
            else:
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value)
            else:
                self.right = Node(value)

def built_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root

def one_child_search(tree):
    if tree:
        one_child_search(tree.left)
        if (tree.left and not tree.right) or (tree.right and not tree.left):
            print(tree.data, end=" ")
        one_child_search(tree.right)

numbers = [int(i) for i in input().split()]
numbers = numbers[:numbers.index(0)]

tree = built_tree(numbers)
one_child_search(tree)
