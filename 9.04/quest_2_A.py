from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def display_voice(self):
        pass
    
class Dog(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.voice = "GAV!!!"
    
    def display_voice(self):
        super().__init__(self)
        print('Voice of ', self.name, ' is ', self.voice )
    
class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, name)
        self.voice = "Miyay"
    
    def display_voice(self):
        super().__init__(self)
        print('Voice of ', self.name, ' is ', self.voice )
    
first_animal = Dog('Sharik')
second_animal = Cat('Vasya')

first_animal.display_voice()
second_animal.display_voice()




