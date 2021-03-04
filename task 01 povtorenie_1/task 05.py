def P(k):
    answer = 1
    for n in range(1, k+1):
        answer *= (n + 3**n)/(n + 5**(2 * n))

    return(answer)

print(P(int(input("Enter k value: "))))
