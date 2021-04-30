from datetime import date

cars_count = 0

class Car:
    def __init__(self, name, year, color):
        global cars_count
        cars_count += 1

        self.__name = name
        self.__year = year
        self.__color = color

    # метод отображающий все характеристики машины

    def show(self):
        print(
            "name:", self.__name +
            "; year:", str(self.__year) +
            "; age:", str(date.today().year - self.__year) +
            "; color:", self.__color
        )

    # откуда и куда едет машина

    def places(self, from_place, to_place):
        print("car", self.__name, "is moving from", from_place, "to", to_place)

    # возраст машины

    def get_age(self):
        print(date.today().year - self.__year)

    # геттеры и сеттеры даты и цвета

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


car = Car("BMW", 2017, "red")
car.show()

car.set_year(2020)
car.color = "yellow"
car.show()

car.places("Ivanovo", "Moscow")

car2 = Car("Audi", 2007, "black")
car2.show()

car3 = Car("Tesla", 2019, "white")
car3.show()

print("cars count:", cars_count)
