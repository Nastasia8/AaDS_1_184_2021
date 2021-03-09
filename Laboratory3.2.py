x=["Clematis", "Dahlia", "Rose", "Iris", "Chrysanthemum", "Freesia", "Astilba", "Lily", "Peony"]
y=[]
for word in x:
    y.append(word[-1])
print([word[-1] for word in x])    
print(list(map(lambda x: x[-1],x)))
