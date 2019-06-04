import random
def randInt(min=0, max=100):
  
  if min > max and max < 0:
    temp = max
    max = min
    min = temp
  max = max - min
  num = random.random() * max + min
  return int(num)
# print(randInt())                   # should print a random integer between 0 to 100
# print(randInt(max=50))             # should print a random integer between 0 to 50
# print(randInt(min=50))             # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
# print(randInt(min=50, max=0))
print(randInt(min=50, max=-1))