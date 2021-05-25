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
        if self.data == value:
            return
        if value < self.data:
            if self.left:
                self.left.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.left = Node(value)
        else:
            if self.right:
                self.right.add(value, depth+1)
            else:
                if Node.__height < depth:
                    Node.__height = depth
                self.right = Node(value)

    def find_forks(self):
        if self.left:
            self.left.find_forks()
        if self.left and not self.right:
            print(self.data)
        if self.right and not self.left:
            print(self.data)
        if self.right:
            self.right.find_forks()

def build_tree(elmnt):
    tree = Node(elmnt[0])
    for i in range(1, len(elmnt)-1):
        tree.add(elmnt[i], 1)
    return tree

lisst = list(map(int, input().split()))
tree = build_tree(lisst)
tree.find_forks()