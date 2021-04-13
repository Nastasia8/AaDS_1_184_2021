def Fun1():
    x=int(input ("Vvedite chislo = "))
    while x != 1:
        if x % 2 == 0:
            x=x/2
        else:
            x=((x*3)+1)/2
        print (x)
Fun1()