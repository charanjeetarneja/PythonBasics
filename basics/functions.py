print('#1 Bsaic Function')


def hello_func(str):
    return str

print(hello_func('Hello World!'))

print('#2 Bsaic Function with two parameters')

def hello_func2(greeting, name='You'):
    return ('{}, {}').format(greeting, name)

print(hello_func2('Hi', 'Charan'))
print(hello_func2('Hi'))

print('#3 Bsaic Function with multiple dynamic arguments & key value pair arguments')

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Arts', name='John', age=22)

courses = ['Math', 'Arts']
info = {'name': 'John', 'age': 32}

student_info(*courses, **info)

########################################

print("#4 Complex function")

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(days_in_month(2020, 2))

print("#5 Recursive function 0,1,1,2,3,5,8")

def fibn(num):
    if num<0:
        print('give a positive number')
    elif num==1:
        return 0
    elif num==2:
        return 1
    else:
        return fibn(num-1)+fibn(num-2)

print(fibn(7))


