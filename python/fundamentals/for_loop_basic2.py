# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]
def biggie_size(p_list):
  for i in range(len(p_list)):
    if p_list[i] > 0:
      p_list[i] = 'big'
  return p_list

print(biggie_size([-1,3,5,-5]))

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
def count_positives(p_list):
  count = 0
  for v in p_list:
    if v > 0:
      count += 1
  p_list[-1] = count
  return p_list

print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7
def sum_total(p_list):
  sum = 0
  for val in p_list:
    sum += val
  return sum

print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))
# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5
def average(p_list):
  sum = 0
  for val in p_list:
    sum += val
  avg = sum / len(p_list)
  return avg
print(average([1,2,3,4]))

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0
def length(p_list):
  return len(p_list)

print(length([37,2,1,-9]))
print(length([]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False
def minimum(p_list):
  min = p_list[0]
  for val in p_list:
    if min > val:
      min = val
  return min
print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False
def maximum(p_list):
  max = p_list[0]
  for val in p_list:
    if max < val:
      max = val
  return max
print(maximum([37,2,1,-9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }
def ultimate_analysis(p_list):
  d_list = {'average': 0, 'minimum': p_list[0], 'maximum': p_list[0], 'length': len(p_list) }
  d_list['minimum'] = p_list[0]
  sum = 0
  for i in range(len(p_list)):
    sum += p_list[i]
    if d_list['minimum'] > p_list[i]:
      d_list['minimum'] = p_list[i]

    if d_list['maximum'] < p_list[i]:
      d_list['maximum'] = p_list[i]
    
  d_list['average'] = sum / len(p_list)
  
  return d_list
print(ultimate_analysis([37,2,1,-9]))
# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]
def reverse_list(p_list):
  start = 0
  end = len(p_list) - 1
  mid = len(p_list) / 2
  while (start < mid):
    temp = p_list[start]
    p_list[start] = p_list[end]
    p_list[end] = temp

    start += 1
    end -= 1

  return p_list

print(reverse_list([37,2,1,-9]))