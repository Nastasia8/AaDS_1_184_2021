from math import*
def funct(p,n,m):
    i=15
    s=p*(1+(i/100)/(m/12))**(m/(12*n))
    print("Стоимость =",s)

p = int(input("сумма вклада ="))
n = int(input("количество лет="))
m = int(input("количество начислений процентов в год ="))
funct(p, n, m) 
