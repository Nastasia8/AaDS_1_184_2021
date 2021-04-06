numbers = [15, 86, 9, 21, -97, -88, 0, -27, 63, -17, -44, -5]
dct = {}

for i in numbers:
    if i < 0:
        dct[i] = 'negative'
    elif i>0:
        dct[i] = 'positive'
    elif i==0:
        dct[i] = 'zero'

print(dct)

print({number: '+' if number > 0 else '-' if number < 0 else 'zero' for number in numbers})