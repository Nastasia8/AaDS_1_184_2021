def tupleCreate(numbers):
    numbers.sort()
    turpled = tuple(numbers)
    return turpled
count = int(input("Count: "))
numbers = []
for i in range(count):
    numbers.append(int(input()))
print(tupleCreate(numbers))