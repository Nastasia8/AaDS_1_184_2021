first = input()
second = input()
li = list()
for n in range(len(first)-len(second)+1):
  if first[n:len(second)+n]==second:
    li.append(n)
print(*li)