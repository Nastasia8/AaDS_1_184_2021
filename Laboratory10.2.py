text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(", ")
a = {}
for word in text:
    if word in a:
        a[word] += 1
    else:
        a[word] = 1
print(a)
b = {}
for word in text:
    b[word] = b.get(word, 0) + 1
print(b)
print({word: text.count(word) for word in text})
