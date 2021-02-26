N = int(input("Введите N: "))
a = [0]*N
for i in range(N):
    print("a[", i, "]=", sep="", end="")
    a[i]=int(input())
print(a)
for i in range(N-1):
    for j in range(N-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)
