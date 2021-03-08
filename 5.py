from math import*
def funct(x,y,z):
    i=15
    s=x*(1+(i/100)/(z/12))**(z/(12*y))
    print("Стоимость =",s)

x = int(input("сумма вклада ="))
y = int(input("количество лет="))
z = int(input("количество начислений процентов в год ="))
funct(x, y, z) 
