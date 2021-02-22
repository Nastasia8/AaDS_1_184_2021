import math
print("Print X and Y number, and procedure number:")
print("Procedures:")
print("1 - addition\n2 - subtraction (x - y)\n3 - multiplication\n4 - division (x/y, y != 0)\n5 - raised X to the power of Y")
x = int(input("X = "))
y = int(input("Y = "))
procedure = 0
answer = 0
while (procedure > 5 or procedure < 1):
    procedure = int(input("Procedure number: "))
    if not 1 <= procedure <= 5:
        print('Only numbers between 1 and 5 are accepted, try again')
if procedure == 1:
    answer = x + y
elif procedure == 2:
    answer = x - y
elif procedure == 3:
    answer = x * y
elif procedure == 4:
    if y == 0:
        print("Y could not be equal 0! Try again.")
    else:
        answer = x / y
elif procedure == 5:
    answer = math.pow(x, y)
print("Answer = ", answer) 
