class Employee:
    def __init__(self, name, surname, experience,position,address, phone_number, n_h, c_h ):
        self.__name = name
        self.__surname = surname
        self.__experience = experience
        self.__position = position
        self.__address = address
        self.__phone_number = phone_number
        self.__n_h = n_h
        self.__c_h = c_h
    def salary(self):
        self.__salary = self.__n_h*self.__c_h
        return self.__salary
    def premium (self):
        if (self.__experience > 1) and (self.__experience <= 3):
            return self.__salary*1.03
        elif (self.__experience > 3) and (self.__experience <= 6):
            return self.__salary*1.05
        elif (self.__experience > 6) and (self.__experience <= 9):
            return self.__salary*1.07
        else:
            return self.__salary*1.13
    def show(self):
        print(self.__name, self.__surname, "hold the position of", self.__position, "\nHis experiense is", self.__experience,"\nAddress:", self.__address, "\nPhone number:",self.__phone_number, "\nSalary:", self.salary(), "\nPremium:", self.premium())
first = Employee("Anton", "Braginsky",5, "painter", "Voronezh", "89994241006", 20, 150)
first.show()