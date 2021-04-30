class Employee:
    def __init__(self, first_name, last_name, seniority, position, address, phone, hours, salary):
        self.__first_name = str(first_name)
        self.__last_name = str(last_name)
        self.__seniority = seniority
        self.__position = str(position)
        self.__address = str(address)
        self.__phone = str(phone)
        self.__hours = hours
        self.__salary = salary

    def show(self):
        print(
            self.__first_name,
            self.__last_name,
            "working as a", self.__position,
            "for",  self.__seniority
        )
        print(
            "Address:", self.__address +
            "; Phone number:", self.__phone +
            "; Hours per day:", str(self.__hours) +
            "; Salary per hour:", self.__salary
        )

    def get_salary(self):
        return int(self.__hours * self.__salary)

    def bonus(self):
        years = self.__seniority
        if years >= 10:
            print(self.get_salary() * 0.13,"(13%)")
        elif years >= 6:
            print(self.get_salary() * 0.7, "(7%)")
        elif years >= 3:
            print(self.get_salary() * 0.5, "(5%)")
        else:
            print(int(self.get_salary() * 0.3), "(3%)")

Nikita = Employee(
    "Nikita",
    "Baranov",
    1,
    "Student",
    "Ivanovo",
    "+7(915)818-40-95",
    8,
    419
)

Nikita.show()
print(Nikita.get_salary())
Nikita.bonus()
