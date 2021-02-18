########## TASK 1 ##########

text = "The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
a = 0
s = 0
for letter in text:
    if letter == "a":
        a += 1
    elif letter == "s":
        s += 1
print("a count:", a)
print("s count:", s)

########## TASK 2 ##########

import math

def calculate(l, g):
    if l * g > 0:
        return 2 * math.pi * math.sqrt(l * g)
    else:
        print("error")

print("Answer :", calculate(int(input("Enter l value: ")), int(input("Enter g value: "))))

########## TASK 3 ##########

def calculate(a, b, operation):
    if operation == 1:
        return(a + b)
    elif operation == 2:
        return(a - b)
    elif operation == 3:
        return(a * b)
    elif operation == 4:
        if b != 0:
            return (a / b)
    else:
        print("error")
        return 0

print("Answer:", calculate(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter operstion: "))))

########## TASK 4 ##########

#Zadanie neponyatnoe

########## TASK 5 ##########

def P(k):
    answer = 1
    n = 1
    for i in range(0, k):
        answer *= (k + 3**k)/(n + 5**(2 * n))

    return(answer)

print(P(int(input("Enter k value: "))))

########## TASK 6 ##########

def nechetCount(nechetFrom, nechetTo):
    answer = 0
    for i in range(nechetFrom, nechetTo):
        if i % 2 == 1:
            answer += 1
    return(answer)

print(nechetCount(int(input("Nechet from: ")), int(input("to: "))))

########## TASK 7 ##########

import math

def roots(x, y, z):
    D = y**2 - 4 * x * z
    if D < 0:
        print("No roots")
    elif D == 0:
        print("root =", -y / (2 * x))
    else:
        print("solution 1 = ", (-y + math.sqrt(D))/(2 * x))
        print("solution 2 = ", (-y - math.sqrt(D))/(2 * x))

roots(int(input("Enter x: ")), int(input("Enter y: ")), int(input("Enter z: ")))

########## TASK 8 ##########

def mlt6Number(number):
    if number // (10**6) == 0 and number % (10**5) != number:
        answer = 1
        for i in range(1, 6+1):
            answer *= number % (10**i) // (10**(i-1))
        return answer
    else:
        print("error")

print("Answer:", mlt6Number(int(input("Enter 6-digit number: "))))
