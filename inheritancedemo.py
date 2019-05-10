import Staff

peter = Staff.BasicStaff('Peter',0)
john = Staff.ManagementStaff('John', 0, 1000, 0)

print(peter, 'pay=', peter.calculatePay())
print(john, 'pay=', john.calculatePay(),' Bonus=', john.calculatePerfBonus())
