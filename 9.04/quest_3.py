class Employee():
    def __init__(self, name, surname, work_experience, post, adress, phone_number, hours_worked, cost_hour):
        self.name = name
        self.surname = surname
        self.work_experience = work_experience
        self.post = post
        self.adress = adress
        self.phone_number = phone_number
        self.hours_worked = hours_worked
        self.cost_hour = cost_hour
    
    def Salary(self):
        print(int(self.hours_worked) * int(self.cost_hour))
    
    def Prize(self):
        pass

    def Display(self):
        print(f'{self.name} {self.surname} work {self.work_experience}. Work on {self.post} post, live in {self.adress}. Phone number: {self.phone_number}. Today {self.name} work {self.hours_worked} hours.')


first_worker = Employee('Nikita', 'Uzhastin', '0', 'junior', 'Ivanovo', '8900555535', '1', '5')
first_worker.Display()    
