print("TASK 1.1")
a = [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
sum = 0
for i in a[::-1]:
    if i > 0:
        break
    sum += i
print(sum)

print("TASK 1.2")
a=[6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]
sum = 0
i = len(a) - 1
while a[i] < 0:
    sum += a[i]
    i -= 1
print(sum)

print("TASK 2")
def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    return f(n-1) + f(n-2) + f(n-3)
for i in range(1,11):
    print(f(i), end = " ")
print()

print("TASK 3.1")
a = list(range(1,31))
ans = []
def calc(x,y):
    for i in a:
        if i % 2 !=0:
            s = (i**x)**y
            ans.append(s)
        else:
            ans.append(i)
print("Введите степени возведения: ")
calc(int(input()),int(input()))
print(ans)

print("TASK 3.2 list comrehension")
a = list(range(1,31))
print("Введите степени возведения: ")
x = int(input())
y = int(input())
print([(i**x)**y if i%2 == 1 else i for i in range(1,31)])

print("TASK 4")
a = int(input("A="))
b = int(input("B="))

while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
print("NOD:",a+b)
print("Task 4.1")
a = int(input("A="))
b = int(input("B="))
while a!=b:
    if a>b:
        a = a-b
    else:
        b = b-a
print("NOD:", a+b)

print("TASK 5")
a = int(input("Введите а: "))
a = int(input("Введите b: "))

def max_sep(a,b):
    while a != 0 and b != 0:
        if a>b:
            a %= b
        else:
            b %= a
    return a + b
def min_mult(a, b):
    return(a*b)// max_sep(a, b)

print("НОК: ", min_mult(a, b))

print("TASK 6")
def funct(a):
    for i in range(len(a)):
        k = a.count(a[i])
        if k>1:
            a[i]= str(a[i])*k
    return set(a)
b = [1, 2, 3, 2, 4, 3, 4, 4]
print(funct(b))

print("Task 7")

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def m_change(arr):
    for i in range(0, len(a)):
        for j in range(0, len(a)):
            if i == j:
                print(a[i][j]*3)
            else:
                print(a[i][j])
m_change(a)

print("Task 8")
a = [[4, 3, 5, 1], [0, 7, 2, 9], [2, 6, 3, 8]]
b = [[13, 97,56], [17, 23, 85], [22, 45, 66]]
def change_mat(list):
    for i in range(0, len(list)):
        for j in list[i][::-1]:
            print(" ".join(str(l) for l in [j]), end = " ")
        print()
print(change_mat(a))
print()
print(change_mat(b))

print("Task 9")
numbers = [15, 9, -1, 7, -6, 0, 8]
print({number: "+" if number > 0 else "-" if number < 0 else "zero" for number in numbers})

print("Task 9.1")
numbers = [15, 9, -1, 7, -6, 0, 8]
upd = {}
for number in numbers:
    if number > 0:
        upd[number] = "+"
    elif number < 0:
        upd[number] = "-"
    else:
        upd[number] = "0"
print(upd)
