dog = {}

dog['name'] = 'Alaska'
dog['color'] = 'White and black'
dog['breed'] = 'Husky'
dog['legs'] = 4
dog['age'] = 8

student = {
    'first_name': 'Sebastián',
    'last_name': 'Trejo',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'HTML', 'Drive', 'Cook'],
    'country': 'Mexico',
    'city': 'Ags',
    'address': 'Ronda Residencial'
}

print(len(student))
print(student['skills'])
print(type(student['skills']))

student['skills'].append('Play Fifa')
student['skills'].append('Play Grouded')

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

del student['marital_status']

del dog