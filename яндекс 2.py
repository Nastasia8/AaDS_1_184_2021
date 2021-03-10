n = int(input())
m = []
for i in range(n):
    buff  = input().split()
    for i in range(len(buff)):
        buff[i] = int(buff[i])
    m.append(buff)
    
for i in range(n-1):
    for j in range(n-i-1):
      if (m[j][1]<m[j+1][1]):
        m[j],m[j+1]=m[j+1],m[j]
      else :
        if ((m[j][0] > m[j+1][0])and(m[j][1] == m[j+1][1])):
         m[j],m[j+1]=m[j+1],m[j]
for i in range(n):
    print(m[i][0],m[i][1])