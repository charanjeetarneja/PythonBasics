import my_module as mm
from my_module import find_index,test
import sys

courses =['History','Math', 'Physics','CompSci']

index=mm.find_index(courses,'Math')

index_2=find_index(courses,'Math')

print(index)

print(index_2)

print(test)

##Locations where your module is looked for by python
print(sys.path)

import random

random_course=random.choice(courses)

print(random_course)

import math

rads=math.radians(90)

print(math.sin(rads))

import datetime
import calendar

today=datetime.date.today()

print(today)

print(calendar.isleap(2017))

import os

print(os.getcwd())

print(os.__file__)

print(os.environ)