a = int(input("Введите x: "))
b = int(input("Введите y: "))
def func(a,b):
    i = min(a,b)     
    while True:
        if i%a==0 and i%b==0:
            break
        i+=1
    print("Наименьшее общее кратное х и y =", i)    
print(func(a,b))