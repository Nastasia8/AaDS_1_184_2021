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
        today = datetime.datetime.now()

        print(today.year - int(self.date))
    
    def set_color(self, color):
        self.color = color

    def get_date(self):
        print(self.date)
        return self.date

    

first_car = Car('BMW', 'Red', '2001', 'old')
first_car.Display()
first_car.Start_End('Ivanovo', 'Pestyaki')

second_car = Car('Shah', 'Yellow', '1980', 'very old')
second_car.Age()
second_car.Display()

third_car = Car('LADA 7', 'cherry', '2005', 'old')
third_car.Display()
third_car.set_color('Red')
third_car.Display()
