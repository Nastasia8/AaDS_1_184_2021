x = list(range(1, 26))
y=[]
for number in x:
   if number%2==0:
      y.append(number**2)
for number in y:
   print(number)

print([i**2 for i in x if i%2==0])
