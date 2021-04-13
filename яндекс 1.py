n = int(input())
m = input().split()
check = 0
for i in range(n):
    for j in range (n-i-1):
        check = 0
        if (m[j] > m[j+1]):
            check = 1
            m[j],m[j+1]=m[j+1],m[j]
        if (check == 1):
           print(' '.join(m))
        else:
           print(check)