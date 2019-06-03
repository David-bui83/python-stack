# 1. TASK: print "Hello World"
print('hello world')
# 2. print "Hello Noelle!" with the name in a variable
name = "Noelle"
print('Hello', name)  # with a comma
print('Hello ' + name)  # with a +
# 3. print "Hello 42!" with the number in a variable
name = 42
print('The number is', name)  # with a comma
# with a +	-- this one should give us an error!
# print('the number is %d' + name)
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print('I love to eat {}'.format(fave_food1))  # with .format()
print(f'I lave to eat {fave_food2}')  # with an f string

# Figure out how to resolve the error from above, without changing the + sign to a comma
print('The number is %d' % name)

# Store 2 of your favorite in variables, and then use them to print the string "I love to eat {food_one}} and {{food_two}}. with the format method (#4b)"
fave_food1 = 'burger'
fave_food2 = 'hot dog'
print('I love to eat {} and {}'.format(fave_food1, fave_food2))

# Store 2 of your favorite foods in vairables, and the use them to print the string "I love to eat {{food_one}} and {{food_two}}." with f-string (#4b)
fave_food1 = 'taco'
fave_food2 = 'burrito'
print(f'I lover to eat {fave_food1} and {fave_food2}')

# NINJA BONUS: Spend a few minutes playing around with other string methods to see what's out there!
test_string = 'This Is A Test String'
# string.upper()
print(test_string.upper())
# string.lower()
print(test_string.lower())
# string.count(substring)
print(test_string.count('s'))
# string.split(char)
print(test_string.split(' '))
# string.find(substring)
print(test_string.find('is'))
# string.isalnum()
print(test_string.isalnum())
# string.isalpha()
print(test_string.isalpha())
# string.isdigit()
print(test_string.isdigit())
# string.islower()
print(test_string.islower())
# string.isupper()
print(test_string.isupper())
# string.join(list)
print(''.join(test_string))
# string.endswith(substring)
print(test_string.endswith('g'))
