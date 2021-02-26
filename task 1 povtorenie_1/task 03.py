def calculate(a, b, operation):
    if operation == 1:
        return(a + b)
    elif operation == 2:
        return(a - b)
    elif operation == 3:
        return(a * b)
    elif operation == 4 and b != 0:
        return (a / b)
    else:
        print("error")
        return 0

print("Answer:", calculate(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter operation: "))))
