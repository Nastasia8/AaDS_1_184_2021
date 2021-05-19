Array = [] #Создаём пустой массив
length = int(input()) #Ввод кол-ва чисел, которые мы будет вводить
for i in range(length): #Цикл for, который идёт до длинный lenght
    Array.append(input()) #Пишем числа и добавляем их в массив
print("Initial array:") #Выводим на экран Initial array:
print(', '.join(Array)) #Выводятся наши числа через запятую
Count = len(Array[0]) #Длинна первого элемента
Phase=0
Rang=10 #кол-во Busket
for i in range(Count-1,-1,-1): #Цикл for, который идёт в обратном направлении от Count-1 до -1 с шагом -1
    Phase+=1 # Прибавляем к фазе 1
    print('**********') #Выводим **********
    print(f'Phase {Phase}') #Выводим Phase и число фазы
    bucket = [[] for _ in range(Rang)] #Создаём список размером 10 элементов
    for j in range(len(Array)): #Цикл for до конца массива
        bucket[ord(Array[j][i]) - ord('0')].append(Array[j]) #Вычисляем индекс с помощью функции ord и записывает в него j-ый элемент
    for j in range(Rang): #Цикл for до 10
        if len(bucket[j])==0: #Условие при котором длина корзины равна 0
            print(f'Bucket {j}: empty') #Выводим Bucket (номер): empty
        else: #Иначе
            print("Bucket "+str(j)+": ", end='') #Выводим Bucket (номер): 
            for now in range(len(bucket[j])): #Цикл for до длины карзины номера
                print(bucket[j][now],end=', ') #Выводим число,которое находится в карзине
            print() #Переход на новую строку
    p = 0 #Вводим переменную
    for j in range(Rang): #Цикл for до 10
        for k in range(len(bucket[j])): #Цикл до длины корзины
          Array[p] = bucket[j][k] #к массиву переменной p присваивается число из карзины с индуксов j
          p += 1 #Увеличиваем переменную p на едиинцу
 
print('**********') #Выводим на экран **********
print("Sorted array:") #Выводим на экран Sorted array:
print(', '.join(Array)) #Выводим полученный результат