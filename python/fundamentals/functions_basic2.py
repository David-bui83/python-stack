# 1. Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
# Example: countdown(5) should return [5,4,3,2,1]
def count_down(p_num):
  num_list = []
  for num in range(p_num, -1,-1):
    num_list.append(num)
  return num_list

print(count_down(10))

# 2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
def print_and_return(a, b):
  print(a)
  return b

print(print_and_return(1,2))

# 3. First Plus Length - Create a function that accepts a list nad returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
def first_plus_length(p_list):
  return p_list[0] + len(p_list)
print(first_plus_length([1,2,3,4,5]))

# 4. Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values form the original lis that are greater than its 2nd value. Print how many values this is and then return the new list. if the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
def values_greater_than_second(p_list):
  second_value = p_list[1]
  new_list = []
  for num in p_list:
    if num > second_value:
      new_list.append(num)
  return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
#5 Write a function that accepts two integers as parameters: size vand value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]
def length_and_value(l, v):
  new_list = []
  for i in range(l):
    new_list.append(v)
  return new_list
print(length_and_value(4,7))
