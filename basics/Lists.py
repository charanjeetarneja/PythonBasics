courses = ['History','Maths','Physics','CompSci']

print(courses)

print(courses[0])

print(courses[-1])

print(courses[0:2])

print(courses[:3])

print(courses[2:])

courses.append("biology")

print(courses)

courses.insert(2,"Geography")

print(courses)

courses_2 = ['Art','Education']

#courses.insert(1,courses_2)

#print(courses)

courses.extend(courses_2)

print(courses)

courses.remove('Maths')

print(courses)

popped = courses.pop()

print(popped)

courses.sort()

print(courses)

courses.sort(reverse=1)

print(courses)

courses_2.reverse()

print(courses_2)


nums=[1,2,3,4]

print(min(nums))
print(sum(nums))

print(courses.index('Art'))

print('Art' in courses)

print('TArt' in courses)

for item in courses:
    print(item)

for index,item in enumerate(courses, start=1):
    print(index, item)

course_str=' - '.join(courses)

print(course_str)

new_courses=course_str.split(' - ')

print(new_courses)

