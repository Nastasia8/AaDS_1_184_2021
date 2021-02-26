def func(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    elif n == 2:
        return 5
    return func(n-1)+func(n-2)+func(n-3)
    
for i in range(0,11):
    print(func(i), end =  " ")
       
