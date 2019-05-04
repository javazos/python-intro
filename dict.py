student = {'name':'John','age':25,'courses':'Compsci',1:'ex'}
student['phone'] = '555-5555'
student['name'] = 'Jim'
student.update({'name':'Joan','age':26,'courses':'Compsci,History'})

print(student.get('phone','Not Found'))
print(student)
# del student['age']
age = student.pop('age')
print(age)
print(student.keys())

print(student.values())
print(student.items())
for key,value in student:
    print( key,value)