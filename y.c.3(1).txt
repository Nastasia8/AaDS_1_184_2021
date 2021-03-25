a=input()
b=input()
list=list()
for i in range(len(a)-len(b)+1):
  if a[i:len(b)+i]==b:
    list.append(i)
print(*list)