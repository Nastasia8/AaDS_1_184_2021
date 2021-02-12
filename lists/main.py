#TASK_1
from math import sqrt

def Disk(x,y,z):
    return y*y-4*x*z

x = int(input("X="))
y = int(input("Y="))
z = int(input("Z="))
(D) = Disk(x, y, z)

if D<0:
    print("Уравнение не имеет корней")

if D==0:
    print("Уравнение имеет один корень. x = ", round(-y/2*x, 2))

if D>0:
    print("Уравнение имеет два корня: x1=", round(-y+sqrt(D)/2*x, 2), "x2=", round(-y-sqrt(D)/2*x, 2))
print()

#TAKS_2
all_numbers = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
odd_numbers = []

for i in all_numbers:
    if i%2==1:
        odd_numbers.append(i)
print(odd_numbers)

#TAKS_2_1_list
print([i for i in all_numbers if i%2==1])

#Task 3
numbers = list(range(1,26))
for i in numbers:
    if i%2==0:
        print("Число ", i, " в квадрате равно", i*i)

print([i*i for i in numbers if i%2==0])









