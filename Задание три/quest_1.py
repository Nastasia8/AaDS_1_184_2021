arr =  [6, 2, 9, 13, 1, 8, 4, -5, -11, -8, -2, -6]

print(arr)
count = 0
for i in arr[::-1]:
    if i>0:
        break
    count+=i
    
print(count)

i = -1
sum = 0
while arr[i] < 0:
    sum+=arr[i]
    i-=1
print(sum)



