import datetime
import pytz

# dt_today = datetime.datetime.today() #return current local date time with timezone none
# dt_now = datetime.datetime.now()#pass a timezone
# dt_utcnow = datetime.datetime.utcnow()#Tz info
#
# print(dt_today)
# print(dt_now)
# print(dt_utcnow)
#
#
# import sys, setuptools, pkg_resources
# print(sys.path)
# print (pkg_resources.__file__)
# print (setuptools.__file__)

dt = datetime.datetime(2019,5,5,12,30,45,tzinfo=pytz.UTC)
print(dt)
# prefer the following
dt_now = datetime.datetime.now(tz=pytz.UTC)
print("UTC now",dt_now)
print()
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print("utc now2", dt_utcnow)
print()

dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
dt_eastern = dt_utcnow.astimezone(pytz.timezone('US/Eastern'))
print(dt_eastern)


for tz in pytz.all_timezones:
    print('tz: ',tz)
#naive time
dt_toronto = datetime.datetime.now()
dt_shanghai = dt_toronto.astimezone(pytz.timezone('Asia/Shanghai'))
print("Toronto=", dt_toronto)
print("Shanghai:", dt_shanghai)


# localize naive time
dt_markham = datetime.datetime.now()
tz_ca_eastern = pytz.timezone('Canada/Eastern')

dt_markham=tz_ca_eastern.localize(dt_markham); # dt_markham is localized
dt_zurich = dt_markham.astimezone(pytz.timezone('Europe/Zurich'))
print(dt_zurich)


#iso format
print(dt_markham.isoformat())
# strftime - Datetime to String
print(dt_markham.strftime('%B %d,%Y'))
dt_str = "July 26,2019"
# strptime - String to Datetime
strdt = datetime.datetime.strptime(dt_str,'%B %d,%Y')
print(strdt)



