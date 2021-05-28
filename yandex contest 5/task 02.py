class Node:  # класс бинарного дерева
    def __init__(self, data): # инициализация
        self.data = data # элемент для добавления
        self.left = None # элемент слева
        self.right = None # элемент справа

    def add(self, value): # функция добавления
        if self.data == value: # если элемент для добавления равен прошлому элементу тогда
            return # ничего не произойдет
        if value < self.data: # если значение меньше чем предыдущее добавленное
            if self.left: # если есть элемент слева
                self.left.add(value) # слева добавить элемент
            else: # иначе
                self.left = Node(value) # слева добавить бинарное дерево с элементом
        else: # иначе
            if self.right: # если есть элемент справа
                self.right.add(value) # справа добавить элемент
            else: # иначе
                self.right = Node(value) # справа добавить бинарное дерево с элементом

    def check_tree(self): # функция проверки баланса дерева
        if self.left and self.right: # если есть элемент справа и слева тогда
            if abs(height(self.right) - height(self.left)) > 1: # если модуль элементов справа и слева больше 1 тогда
                return "NO" # вывести нет
        else: # иначе
            if not self.right and self.left and height(self.left) > 1: # если нет элемента справа и есть элемент слева и высота дерева больше 1
                return "NO"  # вывести нет
            if not self.left and self.right and height(self.right) > 1: # если нет элемента слева и есть элемент справа и высота дерева больше 1
                return "NO" # вывести нет
        if self.left: # если есть элемент слева
            if self.left.check_tree() == "NO": # и заново проверить бинарное дерево слева
                return "NO" # вывести нет
        if self.right:     # если есть элемент справа
            if self.right.check_tree() == "NO": # и заново проверить бинарное дерево справа
                return "NO" # вывести нет

def built_tree(elements): # функция построение бинарного дерева
    tree = Node(elements[0]) # дерево заканчивается элементом 0
    for i in range(1, len(elements)): # от 1 до коллисечтва введенных элементов
        tree.add(elements[i])  # присовединять элемент из массива под индексом i
    return tree # возвращать дерево

def height(tree): # высота дерева
    if not tree: # если нет дерева
        return 0 # вывести 0
    return (max(height(tree.left), height(tree.right))+1)  # возвратить высоту дерева из максимальной высоты бинарного дерева справа или слева

def main(): # главная функция
    num = list(map(int, input().split())) # ввод всех элементов дерева
    num.pop() # убрать последний элемент из массива
    num = built_tree(num) # построить дерево из значений
    print(num.check_tree()) if num.check_tree() == 'NO' else print("YES") # если дерево сбалансировано вывести да иначе нет

main() # вызов главной функции
