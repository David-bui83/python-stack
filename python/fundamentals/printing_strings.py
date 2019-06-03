# String Literals
print('this ia a sample string')


# Concatenating Strings and Variable with the print function

# Using a comma to print a string and a variable
name = 'Zen'
print('My name is', name)

# Concatinating with a +
name = 'Zen'
print('My name is ' + name)

# String Interpolation - injecting variables in to strings

# F-string(literal String Interpolation) - To constuct an f-string, place an f right before the opening quotation
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")


# String.format() - replace any words that will get their values from vairables with {}. Then call format
# method
first_name = 'Zen'
last_name = 'Coder'
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))

# %-formating - % symbol is used to indicate a placeholder, a %s for a string and %d for a number. a single
# % separates the string to be interpolated from the values to be inserted
hw = 'Hello %s' % 'world'
py = 'I love Python %d' % 3
print(hw, py)

name = 'Zen'
age = 27
print('My name is %s and I\'m %d' % (name, age))

###
# Built in string methods
#
# string.upper(): returns a copy of the string with all the characters in uppercase
# string.lower(): returns a copy of the string with all the characters in lowercase
# string.count(subsrting): returns number of occurrences of substring in the string
# string.split(char): returns a list of values where string is split at the given character. Without a parameter the default split is at every space
# string.find(substring): returns the index of the start of the first occerence of substring within string
# string.isalnum(): returns boolean depending on whether the string's length is > 0 and all characters are alphanumeric (letter and numbers only). Strings that include spaces and puncuation will return False for this method. Similar methods include .isalpha(), .isdigit(), .islower(), .isupper(), and so on. All return booleans.
# string.join(list): returns a string that is all strings within our set (in this case a list) concatenated
# string.endswith(substring): returns a boolean based upon whether the last characters of string match substring
#
###
