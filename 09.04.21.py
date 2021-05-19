#повторение 09.04
#задача 1

s = input().replace(" ", "")
stack = []  #[value, prior]
res_string = []
operations = {"*":3, "/": 3, "+": 2, "-": 2, "(": 1}
for i in s:
    if i == "+-*/()":
        if i == ")":
            while stack[-1][0] != "(":
                res_string.append(stack.pop()[0])
            stack.pop()
            continue
        while stack and stack[-1][1] >= operations[i] and i!="(":
            res_string.append(stack.pop()[0])
        if not stack or stack[-1][1]<operations[i] or i == "(":
            stack.append([i, operations[i]])
    else:
        res_string.append(int(i))
while stack:
    res_string.append(stack.pop()[0])
print(*res_string)


#задача 2
class Animal:
    def __init__(self, name):
        self.__name = name
    def speak(self, voice):
        raise NotImplementedError("Класс - потомок должен реализовать данный метод!!!")
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.__age = 1
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if age>0 and age < 25:
                self.__age = age
            else:
                print("!!!!!!!")
        else:
            print("sdddfdgdfsd!!!")
    def speak(self, voice):
        print("Dog is saying ", voice)
    def show(self):
        print("name: ", self.__name,"age: ", )





