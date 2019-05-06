import sys
sys.path.append('C:\\Users\\cxu\\PycharmProjects\\my_modules')
from my_modules import find_index as fi,test
# from my_modules import *
# import my_modules as mm
courses = ['History','Math','Physics','CompSci']

index = fi(courses,'Math')
# index = fi(courses,'Math')
print(index)
print(test)





print(sys.path)
import random
random_course = random.choice(courses)
print(random_course)

import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))


import datetime_intro
import calendar

today = datetime_intro.date.today()
print(today)

print(calendar.isleap(2019))


import os
print(os.getcwd())
print(os.__file__)


