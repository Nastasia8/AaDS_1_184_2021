class Animal:
    def __init__(self, name):
        self.__name = name

    def speak(self, voice):
        raise NotImplementedError("error 01")

    @property
    def name(self):
        return self.__name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.age = 1

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            if age > 0 and age < 25:
                self.__age = age
            else:
                print("is dead")
        else:
            print("error 02")

    def speak(self, voice):
        print("Dog is saying", voice)

    def show(self):
        print("name:", self.name, "age:", self.age)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self, voice):
        print("Cat is saying", voice)

    def show(self):
        print("name:", self.name)


dog = Dog("Jerry")
dog.speak("gav")

cat = Cat("Tom")
cat.speak("meow")
