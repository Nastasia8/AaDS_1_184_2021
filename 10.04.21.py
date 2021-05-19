from datetime import date
class Car:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year
    def show(self):
        print("name: ", self.__name, "year: ", self.__year, "age: ", date.today().year - self.__year, "color: ", )

    def get_year(self):
        return self.__year

    def get_year(self, year):
        self.__year = year

    @property
    def color(self):
        return self.__color

    @color.selter
    def color(self, color):
        self.__color = color

 car = Car("name", 2010)
 car.show()
 print(car.get_year())
 car.set_year(2020)
 car.show()
 print(car.color)
 car.color = "green"
 car.show()
 #7 3 2 1 9 5 4 6 8
 # pre_order 7 3 2 1 5 4 6 9 8
 # post_order 1 2 4 6 5 3 8 9
 # in_order 1 2 3 4 5 6 7 8 9
 # add()
 # print()
 # search()
 # del()
 # size()
 # heigh()
 class Node:
     __size = 0
     def __init__(self, data):
         self.data = data
         self.left = None
         self.right = None
         Node.__size+=1

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
     def print(self):
         if self.left:
             self.left.print()
         print(self.data, end = " ")
         if self.right:
             self.right.print()

def build_tree(elements):
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root
def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end = " ")
        in_order(tree.right)


def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end=" ")
        in_order(tree.right)


def in_order(tree):
    if tree:
        in_order(tree.left)
        print(tree.data, end=" ")
        in_order(tree.right)


numbers = [int(i) for i in input().split()]
tree = build_tree(numbers)
tree.print()

# # 7 3 2 1 9 5 4 6 8
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
            print(self.data, end = "")
        if self.right:
            self.right.find_fork()



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
tree.print()
print()
print(tree.height+1)
print(height(tree))
print()
tree.find_fork()









