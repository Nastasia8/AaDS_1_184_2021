a = (5, 1, 3, 5, 3, 1, 9, 5, 3, 8, 6, 5, 7)
dict = dict()

for i in range(0, len(a)):
    dict[i] = a[i]
    
sum = 0
mlt = 1

for i in dict:
    sum += dict[i]
    mlt *= dict[i]

print("sum:", sum)
print("mlt:", mlt)
