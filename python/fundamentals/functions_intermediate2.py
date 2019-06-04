# Update Values in Dictionaries and Lists
x = [[5,2,3],[10,8,9]]
students = [{'first_name': 'Michael', 'last_name': 'Jordan'},{'first_name': 'John', 'last_name': 'Rosales'}]
sports_directory = {'baseketball': ['Kobe', 'Jordan', 'James', 'Curry'], 'score': ['Messie', 'Ronaldo', 'Rooney']}
z = [{'x': 10, 'y': 20}]

# 1. Change the value 10 in x to 15. Once you're done, x should now be [[5,2,3],[15,8,9]] 
x[1][0] = 25
print(x)
# 2. Change the last_name of the first student form 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)
# 3. In the sports_directory, change 'Messi' to 'Andres'
sports_directory['score'][0] = 'Andres'
print(sports_directory)
# 4. Change the value 20 in z to 30
z[0]['y'] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary(students):
  for student in students:
    person = []
    for key, val in student.items():
      person.append(key)
      person.append(val)
    print(person[0] + ' - ' + person[1] +', ' + person[2] + ' - ' + person[3])
iterateDictionary(students)

# 3. Get Values from a List of Dictionaries
students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary2(key_name, some_list):
  for items in some_list:
    print(items[key_name])

iterateDictionary2('first_name', students2)
print('----------------------------')
iterateDictionary2('last_name', students2)

# # 4. Iterate Through a Dictionary with List Values
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):

  for key, val in some_dict.items():
    print('\n' + str(len(val)) + ' ' + key.upper() )
    for name in val: 
      print(name)

printInfo(dojo)