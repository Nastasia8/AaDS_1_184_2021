def funct(y,z):
    a=[]
    for x in range (1,31):
        if x%2==1:
            a.append(x**y**z)
        else:
            a.append(x)
        print(a)
    y=int(input("Введите y:"))
    z=int(input("Введите z:"))
    funct(y,z)
    print([number**y**z if number%2==1 else number for number in range(1,31)])



