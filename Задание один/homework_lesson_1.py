print('Task 5')

def Calc(k):
    for n in range(1,k):
        prod = (n+3**n)/(n+5**2*n)
    return prod

k = int(input('K: '))
D =  Calc(k)
print(D)

print('Task 6')

def Func(start, end):
    summa = 0
    all_numbers = list(range(start, end))
    for i in all_numbers:
        if i%2==1:
            summa+=i
    return  summa
start = int(input("Start:"))
end = int(input("End:"))
print(Func(start, end))

print('Task 8')
number = int(input('Введите число: '))
if (number>99999) and (number<1000000):
    while True:
        count = number % 10
        number = number // 10
        if count: break
    while number:
        x = number % 10
        if x:
            count *= x
        number = number // 10
    print(count)
else:
    print('Oh...')




