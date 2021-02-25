first_list = list(range(0,30))
second_list = []

def calc(y, x):
    
    for i in first_list:
        if i%2==1:
             i = i**x**y
             second_list.append(i)
        else:
            second_list.append(i)

x = int(input('X:'))
y = int(input('Y:'))
calc(y, x)
print(second_list)

print([number**x**y if number%2==1 else number for number in range(1,30+1)])

