from abc import ABC, abstractmethod
from math import pi
class Figure(ABC):
    def __init__(self, color):
        self.__color = color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, newcolor):
        self.__color = newcolor
    @abstractmethod
    def perimeter(self, p):
        pass
    @abstractmethod
    def square(self):
        pass
    @abstractmethod
    def info(self):
        print("color: ", self.color)
class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height
        self.type = "Rectangle"
    def perimeter(self):
        return (self.__width + self.__height)*2
    def square(self):
        return self.__width * self.__height
    def info(self):
        print("type:", self.type, "square:", self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()

class Foursquare(Rectangle):
    def __init__(self, width, color):
        super().__init__(width, width, color)
        self.type = "Foursquare"

class Triangle(Figure):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.__a = a
        self.__b = b
        self.__c = c
        self.type = "Triangle"
        self.__p=self.__a + self.__b + self.__c
    def perimeter(self):
        return self.__a + self.__b + self.__c
    def square(self):
        return (((self.__p)/2)*((self.__p)/2 - self.__a)*((self.__p)/2 - self.__b)*((self.__p)/2 - self.__c))**(0.5)
    def info(self):
        print("type:", self.type, "square:", self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()

class Circle(Figure):
    def __init__(self, radius , color):
        super().__init__(color)
        self.__radius = radius
        self.type = "Circle"
    def perimeter(self):
        return 2*pi*self.__radius
    def square(self):
        return pi*(self.__radius**2)
    def info(self):
        print("type:", self.type, "square:", self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()

class Trapezoid(Figure):
    def __init__(self, a, b, c, d, h , color):
        super().__init__(color)
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__h = h
        self.type = "Trapezoid"
    def perimeter(self):
        return self.__a+self.__c+self.__b+self.__d
    def square(self):
        return (self.__h/2)*(self.__a + self.__b)
    def info(self):
        print("type:", self.type, "square:", self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()

second = Foursquare(5, "red")
second.info()

first = Rectangle(10, 5, "green")
first.info()

fird = Triangle(5, 6, 10, "black")
fird.info()

fourth = Circle( 3, "yellow")
fourth.info()

fifth = Trapezoid( 3, 6, 5, 4, 2, "purple")
fifth.info()