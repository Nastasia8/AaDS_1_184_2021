def NOD(x,y):
    while x != 0 and y != 0:
        if x > y:
            x %= y
        else:
            y %= x
    return(x+y)
def NOK(x,y):
    return x*y/NOD(x,y)
x=int(input("Введите x: "))
y=int(input("Введите y: "))
print ("НОК (",x, ";",y, ") =", NOK(x,y))