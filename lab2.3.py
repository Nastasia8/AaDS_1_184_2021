  
a=["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]
b=[]
for word in a:
    b.append(word[-1])
print([word[-1] for word in a])    
print(list(map(lambda x: x[-1],a)))
