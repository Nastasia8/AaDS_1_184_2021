y = int(input("Enter x: "))
z = int(input("Enter z: "))

#1

x = list(range(1, 31))

def degrees(y, z, list):
    for i in range(0, len(list)):
        if list[i] % 2 == 1:
            list[i] = list[i]**z**y
    print(list)

degrees(y, z, x)

#2

print([i**z**y if i % 2 == 1 else i for i in range(1, 30+1)])
