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

    def __repr__(self):
        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
    #
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    def __add__(self, other_emp):
        return self.pay+other_emp.pay
    def __len__(self):
        return len(self.fullname())


emp1 = Employee('caihong', 'xu', 100000)
emp2 = Employee('test', 'user', 100000)

print(int.__add__(1,2))
print('1'.__add__('2'))
print('1'.__len__())
print(emp1.__len__())
print(emp1+emp2)


# print(emp1)
# print(emp2)
# print(repr(emp1))
# print(str(emp1))
# print(emp1.__repr__())
# print(emp1.__str__())