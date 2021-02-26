mn = {"tiger", 0, "leopard", "elephant", 2, 7}
list = [0, 2, 7, 9]

def sameEl(list, el):
    return (False if mn.intersection(list) == set(list) else True)
    
print(sameEl(list, mn))
