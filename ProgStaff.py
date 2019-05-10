class ProgStaff:
    # class variable
    # defined outside any method of the class
    # can be accessed outside the class using the class name
    # Changing it affect all instances of teh class

    companyName = "ProgrammingLab"

    def __init__(self, salary):
        # instance variable
        # defined inside a method in the class and prefixed with the self keyword
        # It can be accessed outside the class by using the instance name
        # Changing it only affects the specific instance

        self.salary = salary

    def printInfo(self):
        print('Company name is ', ProgStaff.companyName)
        print('Salary is ', self.salary)

peter = ProgStaff(2000)
john  = ProgStaff(3000)

peter.printInfo()
john.printInfo()
