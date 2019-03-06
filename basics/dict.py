student= {'name':'john', 'age':25, 'courses':['Maths','CompSci']}

print(student.get('phone','Not Found'))

student['phone']='555'

print(student.get('phone','Not Found'))

student.update({'name':'James','age':26,'sex':'male'})

print(student)

del student['age']

print(student)

phone = student.pop('phone')

print(phone)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

for key in student:
    print(key)

for key,value in student.items():
    print(key, value)