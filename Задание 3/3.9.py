#9
A = [15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5]
d = {}
s=''
print(" С помощью цикла")
for w in A:
    if w <0:
        d[w]=['negative']
        s = w
    elif w==0:
        d[w] = ['zero']
        s = w
    elif w>0:
        d[w] = ['positive']
        s = w
d[s].append(w)
print(d)
print("C помощью Dictionary comperhention")
print({A:"+" if A>0 else "-" if A<0 else "zero" for A in A})

# Дан список состоящий из элементов 15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5.
# Создать словарь -> ключи - элементы списка, значения - positive,negative,zero. Dictionary Comprehension





