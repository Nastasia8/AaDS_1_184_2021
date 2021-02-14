def calc(x, y):
    count = 0
    for number in range(x, y):
        if (number % 2) != 0:
            count = count + 1
    return count
print("Print range.")
x = int(input("From: "))
y = int(input("To: "))
print("Count of odd numbers: ", calc(x, y))