X={0, "Natasha", "Masha", "Dasha"}
Y=[1, "Sasha","Tata","Ilya","Nikita"]
def room58 (X,Y):
    for i in Y:
        if i not in X:
            return False
    return True
print(room58(X,Y))
