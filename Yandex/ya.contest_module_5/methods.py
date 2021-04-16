# pre_order - прямой обход. 7 3 2 1 5 4 6 9 8
# post_order - сначала потомки 1 2 4 6 5 3 8 9 7 
# in_order - дает упорядоченные значения, слева направо 1 2 3 4 5 6 7 8 9  
# add()
# print()
# search()
# del()
# size
# height

class Node:
    __size = 0
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        Node.__size += 1

    @property
    def size(self):
        return self.__size
    
    def add(self, value):
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
            
    def height(tree):
        if tree is None:
            return 0
        return max(height(tree.left), height(tree.right)) + 1    
    
    def find_fork(self):
        if self.left:
            self.left.find_fork()
        if not self.left and not self.right:
            print(self.data)
        if self.right:
            self.right.find_fork()
        
    def search(self, value):
        if self.data == value:
            return True
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_mininmal(self):
        if self.left is None:
            return self.data
        return self.left.find_mininmal()
    
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
            min_value = self.right.find_mininmal()
            self.data = min_value
            self.right = self.right.delete(self.data)
        return self
    
    def print(self):
        if self.left:
            self.left.print()
        print(self.data, end = " ")
        if self.right:
            self.right.print()
    
def build_tree(elements):
    root = Node(elements[0])
    for item in range(1, len(elements)):
        root.add(elements[item])
    return root

numbers = [int(item) for item in input().split()]
tree = build_tree(numbers)

tree.delete(34)