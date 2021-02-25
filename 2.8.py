a = {number: (number + 1) * 4 for number in range(7)}
addition = 0
multiplication = 1
for i in a:
    addition = addition + a[i]
for i in a:
    multiplication = multiplication * a[i]
print("Addition = ", addition)
print("Mumultiplication = ", multiplication)