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
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if (self.left and not self.right) or (not self.left and self.right):
            print(self.data)
        if self.right:
            self.right.find_fork()
def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)-1):
        root.add(elements[i], 1)
    return root
def main():
    numbers = list(map(int, input().split()))
    tree = build_tree(numbers)
    tree.find_fork()
main()
