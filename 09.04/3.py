class Car:

    def __init__ (self,name,color,data):
        self.__name= name
        self.__color=color
        self.__data=data
    def show(self):
        print("name:",__name,"color:",__color,"data",__data)

    def get_year(self):
        return self.__data
    def get_year(self,year):
        self.__data =data

    @property
    def color(self):
        return self.color


car=Car("пежо","красный","02/09/2000")
car.show()
