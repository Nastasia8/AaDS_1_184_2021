import datetime

class Car:
    def __init__(self, name, color, date, new_old):
        self.name = name
        self.color = color
        self.date = date
        self.new_old = new_old
    
    def Display(self):
        print(f'Name of Car: {self.name}, color: {self.color}, release date: {self.date}, car is {self.new_old}')
    
    def Start_End(self, start, end):
        self.start = start
        self.end = end
        print(f'Car goes from {self.start} to {self.end}')
    
    def Age(self):
        print(2021 - int(self.date))
    
    def set_color(self, color):
        self.color = color

    def get_date(self):
        print(self.date)
        return self.date

    

first_car = Car('BMW', 'Red', '2001', 'old')
first_car.Display()
first_car.set_color('black')
first_car.Start_End('Moskow', 'Ivanovo')
first_car.get_date()
first_car.Age()
