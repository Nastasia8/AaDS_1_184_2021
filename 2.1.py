numbers = [5, 0, 7, 3, 6, 14, 96, 23, 82, 53]
# First
odd1 = []
for number in numbers:
    if (number % 2) != 0:
        odd1.append(number)
# Second
odd2 = [number for number in numbers if number % 2 != 0]
# Third
def check(number):
    if number % 2 != 0:
        return number
odd3 = list(filter(check, numbers))
# Fourth
odd4 = list(filter(lambda number: number % 2 != 0, numbers))
# Print
print(odd1)
print(odd2)
print(odd3)
print(odd4)