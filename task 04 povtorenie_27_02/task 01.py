#1

i = int(input("Enter a num:"))
print(i)

def to1(n):
    if n % 2 == 0:
        return n // 2
    else:
        return (n * 3 + 1) // 2

while i != 1:
    i = to1(i)
    print(i)
    
#2

i = int(input("Enter a num:"))
print(i)

def to1(n):
    return n // 2 if n % 2 == 0 else (n * 3 + 1) // 2

while i != 1:
    i = to1(i)
    print(i)
