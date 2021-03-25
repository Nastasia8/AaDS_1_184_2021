number1 = 0
number2 = 0
  text="The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
for i in text:
    if i == "s":
        number1 += 1
    if i == "a":
        number2 += 1
print(number1)
print(number2)