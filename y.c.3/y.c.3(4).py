def cyclic_string(s):
    lenght = len(s)
    k = [0] * lenght
    for i in range(lenght - 1):
        j = k[i]
        while (j > 0) and (s[i + 1] != s[j]):
            j = k[j - 1]
        if (s[i + 1] == s[j]):
            k[i+1] = j + 1
        else:
            k[i + 1] = 0
    return k

inp = str(input())
lenght = len(inp) # lenght присваивает число равное длине вводимой строки
cyclic = cyclic_string(inp) # Переменной cyclic передаётся значение, полученное в функции cyclic_string
print(lenght - cyclic[-1]) # На экран выводится кол-во подстрок из котороых состроит строка