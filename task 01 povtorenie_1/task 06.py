def nechetCount(nechetFrom, nechetTo):
    answer = 0
    for i in range(nechetFrom, nechetTo):
        if i % 2 == 1:
            answer += i
    return(answer)

print(nechetCount(int(input("Nechet from: ")), int(input("to: "))))
