n = int(input())
a = list(map(int, input().split()))[:n]

def main():
    isSorted = False   #переменная, которая отвечает за сортированный массив
    while not isSorted: #до тех пор пока не отсортирован
        isSorted = True
        for i in range(n - 1):
            if a[i] > a[i + 1]: #если элемент не отсортирован, то меняются соседние значения
                a[i], a[i + 1] = a[i + 1], a[i]
                isSorted = False
        print(*a)

if a == sorted(a): #если изначально отсортирован выводим 0
  print(0)
else:
  main()
