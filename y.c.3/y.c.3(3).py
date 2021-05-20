def period(s):
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

lenght = len(inp)
per = period(inp)

#for i in range(lenght - 1, lenght): #Строчка не нужна
    
res = lenght - per[-1] #res присваивается число: длина - результат функции (количество символов вместе)

if (lenght % res == 0): #Условие при котором проверяется целостность длины, зависящей от периода
    print(lenght // res) #Выводится число повторений символов
else:
    print(1) #1 повторение есть всегда