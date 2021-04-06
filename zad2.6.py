a = {"tiger", 0, "leopard", "elephant", 2, 7} 
b = [1, "camel", "elephant", 2, 9]
def animals (a,b):
    for i in b:
        if i not in a:
            return False
    return True
print(animals(a,b))