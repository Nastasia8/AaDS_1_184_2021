b= [5, 6, 9, 6, 3, 5, 2, 5, 1]
def funct(a):
    for i in range(len(a)):
        k=a.count(a[i])
        if k>1:
            a[i]=str(a[i]*k)
    return set(a)
print(funct(b))