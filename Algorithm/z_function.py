def z_function(string):
    array = [0] * len(string)
    start = end = 0
    for i in range(1, len(string)):
        if i <= end:
            array[i] = min(array[i - start], end - i + 1)
        while array[i] + i < len(string) and string[array[i]] == string[array[i] + i]:
            array[i] += 1
        if array[i] + i - 1 > end:
            l = i
            r = array[i] + i - 1

    return array 


string = input()
substring = input()
z = z_function(string + '#' + substring)

for i in range(len(z)):
    if len(string) == z[i]:
        print(i - len(string) - 1, end=" ")