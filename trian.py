def triangle(height):
    current = [1]
    previous = [1]
    print(previous)
    for i in range(height):
        for j in range(int(len(previous)) - 1):
            current.append(previous[j+1] + previous[j])
        current.append(1)
        print(current)
        previous = current
        current = [1]

height = int(input("Triangle height = "))
triangle(height)