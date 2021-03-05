numbers=[15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5]
dict={}
for num in numbers:
    if num > 0:
        dict [num] = "+"
    elif num < 0:
        dict [num] = "-"    
    else:
        dict [num] ="zero"
print({num: "+" if num > 0 else "-" if num < 0 else "zero" for num in numbers})
print (dict)
