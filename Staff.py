class Staff:
    def __init__(self,position,name,pay):
        self._position = position
        self.name = name
        self.pay = pay
        # pass
# special method that is commonly included when we code a class
    def __str__(self):
        # pass
        return "Position={},name={},pay={}".format(self._position,self.name,self.pay)
    def calculatePay(self):
        prompt="\nEnter number of hours worked for {}:".format(self.name)
        hours=input(prompt)
        prompt="Enter the hourly rate for {}:".format(self.name)
        hourlyRate=input(prompt)
        self.pay =int(hours) *int(hourlyRate)
        return self.pay
    @property
    def position(self):
        print("Getter method")
        return self._position

class ManagementStaff(Staff):
    def __init__(self,name,pay,allowance,bonus):
        # super method to call base class __init__ method
        super().__init__('Manager',name,pay)
        self.allowance = allowance
        self.bonus = bonus

    def calculatePay(self):
        basicPay = super().calculatePay()
        self.pay = basicPay + self.allowance
        return self.pay
    def calculatePerfBonus(self):
        prompt="Enter performance grade for {}".format(self.name)
        grade =input(prompt)
        return 1000 if grade == 'A' else 0

class BasicStaff(Staff):
    def __init__(self,name,pay):
        super().__init__("Basic",name,pay)

# officeStaff1 = Staff('Basic','Yvonne',0)
# print(officeStaff1)
# print(officeStaff1.calculatePay())
