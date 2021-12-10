
#CS 101 Lab
#Program 12
#Ryan Lee
#rlhmb@umsystem.edu

'''Create Grades.py. Create Assignment15_Grades.py. Create a function that takes a parameter
of values that is a list of numbers and returns a float that is the total of all numbers in
that list. Create a function that takes a parameter called values that is a list of numbers
and returns a float value that is the average of the numbers in the list. Create a function
that returns the median value of a list. Include unittest and exception handling'''

import math

def total(values : list):
    total = 0
    for i in values:
        total += i
    return total

def average(values : list):
    if len(values) == 0:
        return math.nan
    return total(values) / len(values)

def median(values : list):
    if len(values) == 0 :
        raise ValueError

    values.sort()
    print(values)

    if len(values) % 2 == 1 :
        index = int(len(values) / 2)

        return values[index]
    else:
        index = int(len(values) / 2)
        total = values[index] + values[index - 1]

        return total / 2

