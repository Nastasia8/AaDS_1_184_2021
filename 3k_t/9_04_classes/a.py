class Animal:
    def __init__(self, name):
        self.__name = name
    def speak(self, voice):
        raise NotImplementedError("Класс-потомок должен реализовать данный метод!!!")
    @property
    def name(self):
        return self.__name

class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)
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
                print("This is a very old dog(")
        else:
            print("****")
    def speak(self, voice):
        print("Dog is saying", voice)
    def show(self):
        print("The dog's name is", self.name, "; the age of the animal is", self.age)
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self,name)
    def speak(self, voice):
        print("Cat is saying", voice)
    def show(self):
        print("The cat's name is", self.name)
pesik = Dog("Sharik")
pesik.show()
pesik.speak("gav")
kotik = Cat("Tema")
kotik.show()
kotik.speak("meow")