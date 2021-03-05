words=['Clematis','Dahlia', 'Rose', 'Iris', 'Chrysanthemum','Freesia', 'Astilba','Lily', 'Peony']
print(words)
new_start= words.pop()
new_end= words.pop(0)
words.append(new_end)
words.insert(0,new_start)
print(words)