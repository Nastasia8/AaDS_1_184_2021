x=int(input())
y=int(input())

while x != 0 and y != 0:
    if x > y :
        x %= y 
    else:
        y %= x
gsd = x+y
print(gsd)
