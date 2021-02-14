def calc(x):
    answer = 1
    while x > 0:
        answer = answer * (x%10)
        x = x // 10
    return answer
x = 0
while len(str(x)) != 6:
    x = int(input("X = "))
    if len(str(x)) != 6:
        print("Print six-digit number.")
print("Answer = ", calc(x))