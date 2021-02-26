def mlt6Number(number):
    if number // (10**6) == 0 and number % (10**5) != number:
        answer = 1
        for i in range(1, 6+1):
            answer *= number % (10**i) // (10**(i-1))
        return answer
    else:
        print("error")

print("Answer:", mlt6Number(int(input("Enter 6-digit number: "))))
