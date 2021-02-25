a = { 9, "rose" , 8, "lily", "tulip"}
b = [7, "lily", "narciccus", 6]
def flowers(a,b):
    for i in b:
        if i not in a:
            return False
    return True
print(flowers(a,b))