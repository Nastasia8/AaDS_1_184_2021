#4
words=['Clematis','Dahlia', 'Rose', 'Iris', 'Chrysanthemum','Freesia', 'Astilba','Lily', 'Peony']
print(words)
new_start= words.pop()
new_end= words.pop(0)
words.append(new_end)
words.insert(0,new_start)
print(words)

a = list(range(1,26))
print(a)
a[0],a[-1] = a[-1],a[0]
print(a)

# В списке (из задачи 2) поменять
# местами последний и первый элемент местами. Создать отдельную функцию