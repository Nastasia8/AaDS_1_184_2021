def NOD(x,y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return(x+y)
def NOD2(x,y):
    while x!=0 and y!=0: 
        if x> y:
            if x-y==0:
                return x
            else:
                x=x-y
        else:
            if y-x==0:
                return y
            else:
                y=y-x
x = int(input("Введите x: "))
y = int(input("Введите y: "))
print("1)НОД (",x, ";",y, ") =", NOD(x,y)) 
print("2)НОД (",x, ";",y, ") =", NOD2(x,y))
