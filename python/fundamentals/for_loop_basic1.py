
# Create a Python file called for_loop_basic1.py that performs the folowing tasks.

# 1. Basic - Print all integers from 0 to 150.
def printIntFrom0To150():
    for num in range(151):
        print(num)

printIntFrom0To150()
# 2. Multiples of five - Print all the mulitples of 5 from 5 to 1,000
def printMultOf5():
    for num in range(5, 1001, 5):
        print(num)

printMultOf5()

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. if divisible by 10, print "Coding Dojo".
def countingTheDojoWay():
    for num in range(1, 101):
        if not (num % 10) and not (num % 5):
            print(f'The num is {num} and the word is Coding Dojo')
        elif (num % 10) and not (num % 5):
            print(f'The num is {num} and the word is Coding')

countingTheDojoWay()

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.


def thatSuckersHuge():
    for num in range(500001):
        if num % 2:
            print(num)


thatSuckersHuge()

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.
def countDownByFours():
    for num in range(2018, 0, -4):
        print(num)

countDownByFours()
# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at low Num and going through highNum, print only the integers that are a multiple of mult. For example. if lowNum=2, highNum=9, and mult=3, the loop should print 2, 6, 9 (on successive lines)
def flexibleCounter():
    lowNum = 2
    highNum = 9
    mult = 3
    for num in range(lowNum, highNum + 1):
        if not num % mult:
            print(num)

flexibleCounter()
