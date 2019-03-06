cs_courses={'History','Math','Phyrics','CompSci','Math'}
art_courses={'History','Math','Art','Design'}


print(cs_courses)

print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))

print(cs_courses.difference(art_courses))

print(cs_courses.union(art_courses))

empty_list=list()

empty_tuple=tuple()

empty_set=set()

empty_set_1={}

print(type(empty_set_1))