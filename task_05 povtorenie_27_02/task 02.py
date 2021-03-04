#1

a = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
b = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]

def toMaxLenght(list, symbol):
    maxLenght = 0
    for i in range(0, len(list)):
        if len(list[i]) > maxLenght:
            maxLenght = len(list[i])

    for i in range(0, len(list)):
        while(len(list[i]) < maxLenght):
            list[i] += symbol
    print(list)

toMaxLenght(a, "$")
toMaxLenght(b, "#")

#2

a = ["Bass", "Roach", "Catfish", "Trout", "Mackerel",  "Anchovy"]
b = ["Clematis", "Dahlia", "Rose", "Chrysanthemum", "Freesia", "Lily", "Peony"]

def toMaxLenght(list, symbol):
    list.sort(key = len)
    list = list[::-1]

    for i in range(0, len(list)):
        list[i] = list[i].ljust(len(list[0]), symbol)

    print(list)

toMaxLenght(a, "$")
toMaxLenght(b, "#")
