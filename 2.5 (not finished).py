a = {"tiger", 0, "leopard", "elephant", 2, 7}
b = {1, "camel", "elephant", 2, 9}
union = a | b
crossing = a & b
print("Union: ", union)
print("Crossing: ", crossing)

union2 = []
crossing2 = []
for i in a:
    union2.append(i)
for i in b:
    union2.append(i)
print("Union 2:", union2)