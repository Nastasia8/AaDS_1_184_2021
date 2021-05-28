class Node:  #Создаём класс
    def __init__(self, data): #Функция-конструктор
        self.data = data
        self.left = None
        self.right = None

    def add(self, data): #Функция, с помощью которой добавляется элемент
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add(data)
            else:
                self.left = Node(data)
        else:
            if self.right:
                self.right.add(data)
            else:
                self.right = Node(data)

def height(tree): #Функция, с помощью которой находится высота дерева
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1

def build_tree(elements): #Функция постройки дерева
    root = Node(elements[0])
    for i in range(1, len(elements)):
        root.add(elements[i])
    return root

def balance(tree): #Функция, которая проверяет дерево на сбалансированность: Должны выполниться 2 условия: 1)Высота правого и левого поддерева не должны отличаться более чем на 1. 2) оба поддерева должны быть сбалансированными
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and balance(tree.right) and balance(tree.left)):
        return True # True если условие выполняется
    return False #False если условие не выполняется

def main():
    n = [int(i) for i in input().split()]
    n.pop()
    tree = build_tree(n)

    if balance(tree): 
        print("YES") #Если в прошлой фунции возвращалось True, то на экран выводится Yes
    else:
        print("NO") #Если в прошлой фунции возвращалось False, то на экран выводится No

main()