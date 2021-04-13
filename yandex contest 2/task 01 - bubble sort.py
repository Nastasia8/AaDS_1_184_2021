size = int(input())
a = list(int(i) for i in input().split(" "))[:size]
sorted = False
wasSorted = True

while sorted == False:
    sorted = True
    for i in range(1, size):
        if a[i - 1] > a[i]:
            a[i], a[i - 1] = a[i - 1], a[i]
            sorted, wasSorted = False, False
            print(" ".join(map(str, a)))

if wasSorted:
    print("0")
