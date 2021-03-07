n = int(input())
a = []
for i in range(n):
    k  = input().split()
    for i in range(len(k)):
        k[i] = int(k[i])
    a.append(k)

for i in range(n-1):
    for j in range(n-i-1):
      if (a[j][1]<a[j+1][1]):
        a[j],a[j+1]=a[j+1],a[j]
      elif ((a[j][1] == a[j+1][1]) and (a[j][0] > a[j+1][0])):
        a[j],a[j+1]=a[j+1],a[j]
for i in range(n):
    print(a[i][0],a[i][1])

