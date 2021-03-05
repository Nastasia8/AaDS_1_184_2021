def func(l,s):
    max=len(l[0])
    for i in range(1,len(l)):
        if max < len(l[i]):
            max=len(l[i])
    for i in range(len(l)):
        if max > len(l[i]):
            l[i]+=s*(max-len(l[i]))
    return(l)
a=["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
b=["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]
print(func(a,"&"))
print(func(b,"&"))