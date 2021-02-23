#10
d={}
count = 0
text = "Smile, word, Thank, you, smart, Word, smile, Dog, Cat, word, you, cat, he, thank, You, She, hello, she, smile, thanks, dog, Hello, You, and, He, word".lower().split(', ')
print({word: text.count(word) for word in text})

# На основе исходного текста сформировать словарь,
# в качестве ключа будет использоваться слово из текста
# , а в качестве значения - число вхождений данного слова (ключа) в тексте