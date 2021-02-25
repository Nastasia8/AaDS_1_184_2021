text = "The tiger once ranged widely from the Eastern Anatolia Region in the west to the Amur River basin, and in the south from the foothills of the Himalayas to Bali in the Sunda islands."
a = 0
s = 0
for word in text:
    if word == "a":
        a = a + 1
    elif word == "s":
        s = s + 1
print("'a' count = ", a)
print("'s' count = ", s)