def findS(P, m, n):
    i = 15
    if P > 0 and (m == 3 or m == 6 or m == 12) and n > 0:
        return P * (1 + (i/100)/(m/12))**(m/12*n)
    else:
        print("error")
        return 0

print("S =", findS(int(input("Enter P")), int(input("Enter m")), int(input("Enter n"))))
