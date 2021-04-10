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
        salary = int(self.hours_worked) * int(self.cost_hour)
        self.salary = salary
        print(f'{self.name} salary: {self.salary}')
    
    def Prize(self):
        if (int(self.work_experience) > 1) and (int(self.work_experience) <= 3):
            print(self.salary + (self.salary / (3*100)))
        elif (int(self.work_experience) > 3) and (int(self.work_experience) <= 6):
            print(self.salary + (self.salary / (5*100)))
        elif (int(self.work_experience) > 6) and (int(self.work_experience) <= 9):
            print(self.salary + (self.salary / (7*100)))
        elif (int(self.work_experience) >= 10):
            print(self.salary + (self.salary / (13*100)))
        

    def Display(self):
        print(f'{self.name} {self.surname} work {self.work_experience} years. Work on {self.post} post, live in {self.adress}. Phone number: {self.phone_number}. Today {self.name} worked {self.hours_worked} hours.')


first_worker = Employee('Nikita', 'Uzhastin', '2', 'junior', 'Ivanovo', '8900555535', '6', '30')
first_worker.Salary()
first_worker.Prize()   
first_worker.Display() 
