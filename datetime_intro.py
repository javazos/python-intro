#Dates, Times, Timedeltas and Timezones
import datetime
d=datetime.date(2019, 5, 5)
print(d)
tday = datetime.date.today()
# print(tday.day)
# print(tday.isoweekday())
# print(tday.weekday())
# print(tday.year)
# print(tday.month)
# print(dir(datetime))


tdelta = datetime.timedelta(days=7)
print(tday+tdelta)
print(tday-tdelta)


# date2 = date1 + timedelta
# timedelta = date1 - date2

bday = datetime.date(2019,9,1)
till_bday = bday - tday
print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())



t =datetime.time(9,30,45,10000)
print(t)
print(t.hour)

dt =datetime.datetime(2019,5,5,9,30,45,10000)
print(dt)
print(dt.date())
print(dt.year)


dt2=dt+tdelta
print(dt2)

dt3=dt+datetime.timedelta(hours=12)
print(dt3)

