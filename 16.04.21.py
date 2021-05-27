class Node:
    __size = 0
    __height = 0

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

    def add(self, value, depth):
        if value == self.data:
            return
        if value < self.data:
            if self.left:
                self.left.add(value, depth + 1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value, depth + 1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.right = Node(value)

    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end=" ")
        if self.right:
            self.right.print()

    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if self.left and self.right:
            print(self.data, end="")
        if self.right:
            self.right.find_fork()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete(self, value):
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        else:
            if self.right is None and self.left is None:
                return None
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            min_value = self.right.find_min()
            self.data = min_value
            self.right = self.right.delete(self.data)
        return self

def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right) + 1)

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i], 1)
    return root

def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end=" ")
        in_order(tree.right)

def pre_order(tree):
    if tree:
        print(tree.data, end=" ")
        pre_order(tree.left)
        pre_order(tree.right)

def post_order(tree):
    if tree:
        post_order(tree.left)
        post_order(tree.right)
        print(tree.data, end=" ")

numbers = [int(i) for i in input().split()]
tree = build_tree(numbers)

tree.find_fork()



