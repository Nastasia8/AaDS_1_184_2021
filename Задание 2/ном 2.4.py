#4
words=['Clematis','Dahlia', 'Rose', 'Iris', 'Chrysanthemum','Freesia', 'Astilba','Lily', 'Peony']
print(words)

def zamena(words):
    new_start= words.pop()
    new_end= words.pop(0)
    words.append(new_end)
    words.insert(0,new_start)
print(words)
zamena(words)

# В списке (из задачи 2) поменять
# местами последний и первый элемент местами. Создать отдельную функцию