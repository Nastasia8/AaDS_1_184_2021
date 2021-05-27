a = {1:18, 2:9, 3:14, 4:7.65, 5:-10}
s = 0
p = 1
for n in a:
    s = s + a[n]
    p = p*a[n]
print("s =", s, "\np =",p)
