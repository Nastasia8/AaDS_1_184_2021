string = input()

string.replace(" ","")

stack = []

for i in string:
    if i.isdigit() == True:
        stack.append(int(i))
    
    if i == '+':
        first_number = stack.pop()
        second_number = stack.pop()
        new_number = first_number + second_number
        stack.append(new_number)
    elif i == '-':
        first_number = stack.pop()
        second_number = stack.pop()
        new_number = second_number - first_number
        stack.append(new_number)
    elif i == '*':
        first_number = stack.pop()
        second_number = stack.pop()
        new_number = first_number * second_number
        stack.append(new_number)
    elif i == '/':
        first_number = stack.pop()
        second_number = stack.pop()
        new_number = first_number // second_number
        stack.append(new_number)

print(stack)

    
    

