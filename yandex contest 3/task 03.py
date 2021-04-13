a = input()
max = 1

def checkForSize(size):
    slice = a[0:size]
    count = 1
    for i in range(1, len(a)//size):
        if slice == a[size*i : size * (i+1)]:
            count += 1
            
    if count == len(a)//len(slice) and len(a) == len(a)//len(slice) * size:
        return True
    else:
        return False

for i in range(1, len(a)//2 + 1):
    if len(a) % i == 0:
        if checkForSize(i) and len(a)//i > max:
            max = len(a)//i
        
print(max)
