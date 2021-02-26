#6
def funct(a):
    for i in range(len(a)):
        k=a.count(a[i])
        if k>1:
            a[i]=str(a[i])*k
    return set(a)

b=[1,2,3,5,6,7,6,3,2,1,1,1,2,3]
print(funct(b))

#


