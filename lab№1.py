from math import *
#1-ая задача
a = "The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands"
a=a.lower()
a=a.replace(' ', '')
d=0
for i in a :
  if i == "a" or i == "s":
    d+=1
print (d)
#2-ая задача
g=9.8
l=float(input("Введите длину маятника l "))
T=2*pi*sqrt(l/g) 
print(T)
#3-ая задача
def Oper():
  x=float(input("Ввод первого числа "))
  y=float(input("Ввод второго числа "))
  c=int(input("Ввод номера операции "))
  if c == 1:
    print(x+y)
  if c == 2:
    print(x*y)
  if c == 3:
    print(x/y)
  if c == 4:
    print(x-y)
  if c == 5:
    print(x**y)
Oper()
#4-ая задача
def econom():
  I=15
  P=int(input("ВВедите кол-во рублей "))
  n=int(input("ВВедите кол-во месяцев "))
  m=2
  S=P*(I+((1/100)/(m/12))**(m/12*n))
  print(S)
econom()
#5-ая задача
def chilsr():
  k=int(input("ВВедите число k "))
  x=1
  for n in range(1,k):
    x=x*(n+3**n)/(n+5**(2*n))
  print(x)
chilsr()
#6-ая задача
def diop():
  x=int(input("введите первое число "))
  c=int(input("введите последнее число "))
  z=0
  for i in range (x,c):
    if i % 2 != 0:
      z=z+i
  print(z)
diop()
#7-ая задача
def disk():
  x=int(input("введите число x "))
  y=int(input("введите число y "))
  z=int(input("введите число z "))
  D=y**2-4*x*z
  if D<0:
    print("Корней нет")
  if D==0:
    f1=-y/(2*x)
    print(f1)
  if D>0:
    f1=(-y+sqrt(D))/(2*x)
    f2=(-y-sqrt(D))/(2*x)
    print(f1,f2)
disk()
#8-ая задача
def shest():
  a=(input("введите шестизначное число "))
  p=1
  if (len(a)) == 6:
    for i in a:
      p=p*int(i)
  print(p)
shest()
#9-ая задача
#цикл
a=[5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
b=[]
for num in a:
  if num%2==1:
    b.append(num)
for num in b:
  print(num)
#list comprehension 
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
print([i for i in a if i%2==1])
#использования встроенной функции filter(..., ...)
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
def fun(n):
  return n % 2 == 1
print(list(filter(fun,a)))
#*лямбда-выражений + функция filter(..., ...)*
a = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
print(list(filter(lambda n: n%2==1,a)))
#10-ая задача
a=list(range(1,26))
b=[]
c=[]
for i in a:
  if i % 2==0:
    b.append(i**2)
  else:
    b.append(i)
print(b)
c=([i**2 for i in a if i%2==0])
for i in a:
  if i %2 != 0:
    c.append(i)
print(c)
#11-ая задача
a=["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Astilba", "Lily", "Peony"]
b=[]
for i in a:
  b.append(i[-1])
b.sort()
print(b)
#12-ая задача
a=list(range(1,26))
b=[]
b.append(a[24])
for i in range(1,23):
  b.append(a[i])
b.append(a[0])
print(b)
#13-ая задача
A={"tiger", 0, "leopard", "elephant",  2, 7} 
B={1, "camel", "elephant", 2, 9}
b=[]
c=[]
print(A|B)
print(A&B)
for i in A:
  c.append(i)
for i in B:
  if i not in c:
    c.append(i)
for i in A:
  for g in B:
    if i==g:
      b.append (i)
b=set(b)
c=set(c)
print(c)
print(b)
#14-ая задача
x={1,2,3,4,5,6}
y=[5,6,7,9,10]
def function(x,y):
  for i in y:
    if i not in x:
      return (False)
  return (True)
w=function(x,y)
print(w)
#15-ая задача
a=(5, 1, 3, 5, 3, 1, 0, 9, 5, 3, 8, 6, 5, 7)
b=[]
for i in range(len(a)):
  if a[i]==5:
    b.append(i)
print(b)
#16-ая задача
d = {'dict': 1, 'dictionary': 2, 'prop':3,'like':4}
e = dict.values(d)
x=0
a=1
for i in e:
  x=x+i
for i in e:
  a=a*i
print(x,a)
#17-ая задача
b={}
aw= ["Tom", 23, 170, 65, "Anna", 18, 160, 50, "Alex", 24, 175, 70, "Kim", 33, 180, 57]
s = ""
for i in aw:
    if type(i)==str:
        b[i]=[]
        s=i
    else:
        b[s].append(i)
print(b)
#18-ая задача
az = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(", ")
f = {}
for i in az:
    if i in f:
        f[i] += 1
    else:
        f[i] = 1
print(f)