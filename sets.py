# set - remove duplicates
cs_courses = {'History','Math','Physics','Compsci'}
art_courses = {'History','Art','Physics','Compsci'}

empty_courses = {}  #this is not empty set
empty_set = set()  #this is empty set
cs_courses.add('Python')
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses).union(empty_courses).union(empty_set))
print ('math' in cs_courses)