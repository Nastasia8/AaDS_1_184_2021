#трапеция, треугольник,круг 
from abc import ABC, abstractmethod
from math import pi
class Figure (ABC):
    def __init__(self, color):
        self.__color=color
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, newcolor):
        self.__color=newcolor
    @abstractmethod
    def perimeter(self):
        pass
    @abstractmethod
    def square(self):
        pass
    @abstractmethod
    def info(self):
        print ("color:", self.color)
class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width=width
        self.__height=height
        self.__type="Rectangle"
    def perimeter(self):
        return (self.__width+self.__height)*2
    def square(self):
        return self.__width*self.__height
    def info(self):
        print ("Type:", self.__type, "Square:",self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type = type
class Foursquare(Rectangle):
    def __init__(self, width, color):
        super().__init__(width, width, color)
        self.type="Foursquare"
class Triangle(Figure):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.__a=a
        self.__b=b
        self.__c=c
        self.__type="Triangle"
    def perimeter(self):
        return self.__a+self.__b+self.__c
    def square(self):
        self.__p=self.perimeter()//2
        return (self.__p*(self.__p-self.__a)*(self.__p-self.__b)*(self.__p-self.__c))**(0.5)
    def info(self):
        print ("Type:", self.__type, "Square:",self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()
class Circle(Figure):
    def __init__(self, r, color):
        super().__init__(color)
        self.__r=r
        self.__type="Circle"
    def perimeter(self):
        return round(2*pi*self.__r,2)
    def square(self):
        return round(pi*(self.__r**2),2)
    def info(self):
        print ("Type:", self.__type, "Square:",self.square(), "circumference:", self.perimeter(), end=" ")
        super().info()
class Trapezium(Figure):
    def __init__(self, a, b, c, d, height, color):
        super().__init__(color)
        self.__a=a
        self.__b=b
        self.__c=c
        self.__d=d
        self.__height=height
        self.__type="Trapezium"
    def perimeter(self):
        return self.__a+self.__b+self.__c+self.__d
    def square(self):
        return (self.__a+self.__b)/2*self.__height
    def info(self):
        print ("Type:", self.__type, "Square:",self.square(), "perimeter:", self.perimeter(), end=" ")
        super().info()


rec = Rectangle(5,9, "red")
rec.info()
sq = Foursquare(10, "black")
sq.info()
tr = Triangle(3, 4, 5, "blue")
tr.info()
cir = Circle(8, "purple")
cir.info()
tr = Trapezium(3, 4, 5, 5.1, 5, "yellow")
tr.info()
