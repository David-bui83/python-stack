# Primitive data types - basic building blocks of a language
# Boolean Values - only has two values: True or False
is_hugry = True
has_freckles = False
# Numbers - integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35
weight = 160.57
# Strings - literaal text
name = "Joe Blue"

# Composite Types - are collections composed of primitive types
# Tuples - a type of data that is immutable (can't be modified after its creation) and can hold a group of values. Tuples can contain mixed data types
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])  # output: Bruce
# dog[1] = 'dachshund' # ERROR: cannot be modified ('tuple' object does not support item assignment)

# Lists - a type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])
ninjas[0] = 'Francis'
ninjas.append('Micheal')
print(ninjas)  # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)  # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)  # output: ['Francis', 'Oliver']

# Dictionaries - a group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'  # updates if the key exists
# adds a key-value pair if the key doesn't exist
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')  # removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}


# Common functions

# type - for finding out the data types
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# len - to get the length of lists, dictionaries, tuples, and strings
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))  # output: 11

# Type casting or explicit type conversion
print("Hello" + 42)			# output: TypeErrorcopy
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61
