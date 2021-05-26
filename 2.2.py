n = int(input("Введите количество пар: "))
final_sort = []
for i in range(n):
    a, b = map(int, input("Введите пару: ").split())
    final_sort.append([a, b])
for i in range(n - 1):
    for j in range(n - i - 1):
        if final_sort[j][1] < final_sort[j + 1][1]:
            final_sort[j], final_sort[j + 1] = final_sort[j + 1], final_sort[j]
        if final_sort[j][1] == final_sort[j + 1][1]:
            if final_sort[j][0] > final_sort[j + 1][0]:
                final_sort[j], final_sort[j + 1] = final_sort[j + 1], final_sort[j]
print()
[print(i[0], i[1]) for i in final_sort]