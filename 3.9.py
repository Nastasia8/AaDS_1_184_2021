numbers=[15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5]
print({number: "+" if number>0 else "-" if number<0 else "zero" for number in numbers})
dc={}
for number in numbers:
    if number >0:
        dc[number] = "+"
    elif number <0:
        dc[number] = "-"    
    else:
        dc[number] ="zero"
print (dc)
