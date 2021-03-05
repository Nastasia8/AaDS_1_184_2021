print("task 1")

def funct(num):
    num.sort()
    tu = tuple(num)
    return tu
count = int(input("Count: "))
numbers = []
for i in range(count):
    numbers.append(int(input()))
print(funct(numbers))

print("Task 2")

def funct(g):
    c = [1]
    p = [1]
    print(p)
    for i in range(g):
        for j in range(int(len(p)) - 1):
            c.append(p[j+1] + p[j])
        c.append(1)
        print(c)
        p = c
        c = [1]
g = int(input("Высота треугольника: "))
funct(g)
