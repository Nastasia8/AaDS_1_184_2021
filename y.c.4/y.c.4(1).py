def correct_bracket_sequence(s):
    k = 0
    array = []
    for i in s:
        if (i == '('):
            array.append(i)
        elif (array != []) and (array[-1] == '('):
            array.pop()
        else:
            k += 1
    return k+len(array)

s = str(input())
print(correct_bracket_sequence(s)) 