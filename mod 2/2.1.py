a = input()
arr = input()
strl = arr.split(" ")
res = []
for im in strl:
    res.append(int(im))
a = len(res)
nsw = False
for i in range(0, a-1):
    for j in range(0, a-1-i):
        if res[j] > res[j+1]:
            res[j], res[j+1] = res[j+1], res[j]
            nsw = True
            print(" ".join(map(str,res)))
if nsw == False:
	print("0")
