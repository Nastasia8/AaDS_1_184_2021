a = list(range(1, 26))

#1
chet = []

for item in a:
    if item % 2 == 0:
        chet.append(item**2)
    else:
        chet.append(item)

print(chet)

#2
print(list(chet**2 if chet % 2 == 0 else chet for chet in a))
