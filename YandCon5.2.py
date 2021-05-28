class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def add(self, data):
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


def height(tree):
    if tree is None:
        return 0
    return max(height(tree.left), height(tree.right))+1


def build_tree(elem):
    root = Node(elem[0])
    for i in range(1, len(elem)):
        root.add(elem[i])
    return root


def bal(tree):
    if not tree or ((height(tree.left) == height(tree.right) or height(tree.left)+1 == height(tree.right) or height(tree.left) == height(tree.right)+1) and bal(tree.right) and bal(tree.left)):
        return True
    return False


numb = [int(i) for i in input().split()]
numb.pop()
tree = build_tree(numb)
if bal(tree):
    print("YES")
else:
    print("NO")
