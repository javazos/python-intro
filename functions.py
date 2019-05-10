def myfunc(a,b,c=1,d=2,e=3):
    print(a,b,c,d,e)

def hello_func(*args,**kwargs):
    print(args)
    for arg in args:
        print('{},{}'.format(type(arg), arg))

    print(kwargs)
    print(type(kwargs))
    for kwarg in kwargs.items():
         print('{},{}'.format(type(kwarg),kwarg))
    for kwarg in kwargs.keys():
        print('{},{}'.format(type(kwarg), kwarg))
    for kwarg in kwargs.values():
        print('{},{}'.format(type(kwarg), kwarg))

myfunc(10,20)
hello_func('1','2','3',name='John',Age=22)
in_args = (10,11,12)
in_kwargs = {'course':'math','school':'uot'}
hello_func(in_args,in_kwargs)



#Number of days per month, first value placeholder for index purpose
month_days =[0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
   """Return true for leap year, False for non-leap year"""
   return year%4 == 0 and (year%100!=0 or year%400==0)

def day_of_month(year,month):
    if not 1<=month<=12:
        return 'invalid month'
    if is_leap(year) and month==2:
            return 29
    return month_days[month]

print(day_of_month(2019,2))
