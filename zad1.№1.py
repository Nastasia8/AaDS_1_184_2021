text="The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
a=0
for letter in text:
    if letter == "s":
        a+=1
    if letter == "S":
        a+=1
    if letter == "a":
        a+=1
    if letter == "A":
        a+=1
print(a)
