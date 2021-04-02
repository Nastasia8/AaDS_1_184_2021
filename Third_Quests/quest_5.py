a = int(input('a:'))
b = int(input('b:'))
c = a
d = b

while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a

print('NOK:', c*d/(a+b))