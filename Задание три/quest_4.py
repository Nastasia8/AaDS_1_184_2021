a = int(input('a:'))
b = int(input('b:'))

while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a

print('NOD:', a+b)