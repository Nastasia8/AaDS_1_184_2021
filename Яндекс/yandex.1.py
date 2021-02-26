N = 4
a = [3,4,2,1]

for i in range(N-1):
    for j in range(N-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1] = a[j+1],a[j]
        print(a)


