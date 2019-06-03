# For Loops with Range
for x in range(0, 10, 1):
for x in range(0, 10):  # increment of +1 is impliedcopy
for x in range(10):  # increment of +1 and start at 0 is implied

    # when increment other than +1 is required
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# For Loops through lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz

# OR

for v in my_list:
    print(v)
# output: abc, 123, xyz


# For Loops through dictionaries
# get keys of the dictionary
my_dict = {"name": "Noelle", "language": "Python"}
forcopy k in my_dict:
    print(k)
# output: name, language

# get values of the dictionary
my_dict = {"name": "Noelle", "language": "Python"}
forcopy k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

# another way to iterate through the keys
for key in capitals.keys():
    print(key)
# to iterate through the values
for val in capitals.values():
    print(val)
# to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)

# while loops
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

# while loop with else
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")


# Loop Control
"""
Loops, breaks, and contiues are all a part of control flow

Break - exit the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops. the most common use for the break is when some external condition is triggered. when loops are nested, a break will only exit from the innermost loop

for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

Continue - immediately returns control to the beginning of the loop. In other words, the continues statement rejects, or skips, all teh remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop. Very useful when you want to skip specific iteration(s)

for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y ==copy 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1


"""
