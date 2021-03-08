print("task 1")
# не понял про уникальность элементов, извините... 

print("Task 2")
# я посмотрел, алгоритм действительно совпадает с пашиным, но я полностью понимаю программу и писал ее сам...
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
