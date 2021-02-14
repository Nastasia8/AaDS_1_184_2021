# Дан текст “The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin,
# and in the south from the foothills of the Himalayas to Bali in the Sunda islands.”
# Определить количество букв a и s в тексте. Отобразить полученный результат.
from math import *
a="The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
k=0
e=0
for i in a:
    if i=="a":
     k += 1
    elif i=="s":
     e += 1
print("букв s=",e)
print("букв а=", k)