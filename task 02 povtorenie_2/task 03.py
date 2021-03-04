a = ["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]

#1
w = []
for word in a:
    w.append(word[-1])
    
print(w)

#2
print(list([word[-1] for word in a]))

#3
print(list(map(lambda word : word[-1], a)))
