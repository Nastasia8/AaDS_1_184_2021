import math
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def first():
    i = 0
    for number in numbers:
        if number % 2 == 0:
            numbers[i] = math.pow(number, 2)
        i = i + 1
first()
print("First method:\n", numbers)

# Second method doesn't work for some reason ¯\_(ツ)_/¯
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
def second(number):
    if number % 2 == 0:
        return math.pow(number, 2)
    else:
        return number
numbers = list(filter(second, numbers))
print("Second method:\n", numbers)