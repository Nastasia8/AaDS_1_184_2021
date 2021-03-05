text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(", ")
d1 = {}
#1
for word in text:
    if word in d1:
        d1[word] += 1
    else:
        d1[word] = 1
print(d1)
#2
d2 = {}
for word in text:
    d2[word] = d2.get(word, 0) + 1
print(d2)
#3
print({word: text.count(word) for word in text})
