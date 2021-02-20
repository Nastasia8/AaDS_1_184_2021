text="The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
k=0
n=0
for letter in text:
    if letter == "s":
        k+=1
    if letter == "a":
       n+=1
print(k)
print(n)
