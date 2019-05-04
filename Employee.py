
class Employee:

    num_of_emp = 0
    raise_rate = 0.05

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()== 6:
            return False
        return True
    def __init__(self,first,last,pay):
        self.first = first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        Employee.num_of_emp +=1

    # def __init__(self, from_string):
    #     self.first,self.last,self.pay = from_string.split('-')
    #     Employee.num_of_emp += 1

    @classmethod
    def set_raise_rate(cls,newrate):
        cls.raise_rate = newrate

    @classmethod
    def from_string(cls,instr):
        first,last,pay = instr.split('-')
        return cls(first,last,pay)

    def raise_pay(self):
        # self.pay=self.pay*(1+Employee.raise_rate)
        self.pay = self.pay * (1 + self.raise_rate)
    def fullname(self):
        return self.first+' '+self.last

class Developer(Employee):
    raise_rate = 0.1

    def __init__(self, first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->'+emp.fullname())


# emp3 = Employee.from_string('Joseph-Gosling-300000')

dev1 = Developer('caihong','xu',100000,'Python')
dev2 = Developer('test','user',100000,'Java')

mgr_1 =Manager("Sue","Smith",90000,[dev1])

print(issubclass(Developer,Manager))