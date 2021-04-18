class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, value):  # добавление элемента
            if value == self.data:
                return
            if value < self.data:
                if self.left:
                    self.left.add(value)
                else:
                    self.left = Node(value)
            else:
                if self.right:
                    self.right.add(value)
                else:
                    self.right = Node(value)
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if (not self.left and self.right) or (self.left and not self.right):
            print(self.data, end=" ")
        if self.right:
            self.right.find_fork()

    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end=" ")
        if self.right:
            self.right.print()

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root


numbers = [int(i) for i in input().split()]
numbers.pop()
tree = build_tree(numbers)
tree.find_fork()