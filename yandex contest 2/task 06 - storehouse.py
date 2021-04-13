goodsSize = int(input())
a = list(int(i) for i in input().split(" "))[:goodsSize]
shoppingListSize = int(input())
b = list(int(i) for i in input().split(" "))[:shoppingListSize]

for i in range(0, shoppingListSize):
    a[b[i]-1] -= 1

for i in range(0, goodsSize):
    if (a[i] < 0):
        print("yes")
    else:
        print("no")
