from datetime import date
class Car:
    def __init__(self,name, year,color):
        self.__name=name
        self.__year=year
        self.__color=color
    def show(self):
        print("name:", self.__name, "year:", self.__year, date.today().year-self.__year, "color:", self.__color)
    def way (self, a,b):
        print("The car is coming from",a, "to", b)
    def get_year(self): #вывод значения (получение)
        return  self.__year 
    def set_year(self, year): #изменение значения (установление)
        self.__year=year
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,color):
        self.__color=color

    
    
car=Car("BMW",2015, "black")
car.show()
print(car.get_year())
car.set_year(2020)
car.show()
print(car.color)
car.color= "white"
car.show()
car.way("Ivanovo","Moscow")