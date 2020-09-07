# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.
# Examples

#  round to  (85 - 84 is less than 3)
#  do not round (result is less than 40)
#  do not round (60 - 57 is 3 or higher)
# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

# Function Description

# Complete the function gradingStudents in the editor below.

# gradingStudents has the following parameter(s):

# int grades[n]: the grades before rounding
# Returns

# int[n]: the grades after rounding as appropriate
# Input Format

# The first line contains a single integer, , the number of students.
# Each line  of the  subsequent lines contains a single integer, .

# Constraints

# Sample Input 0

# 4
# 73
# 67
# 38
# 33
# Sample Output 0

# 75
# 67
# 40
# 33

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#
# grades between 0 & 100
# grade below 40 is failing
# if difference betweeen grade and next multiple of 5 is less than 3, round grade up to next multiple of 5
# if grade is less than 38, do no round = failing grade


def gradingStudents(grades):
    newGrades = []
    for grade in grades:
        if grade < 38 or grade % 5 == 0:
            newGrades.append(grade)
        else:
            if (5 - grade % 5) >= 3:
                newGrades.append(grade)
            else:
                new = grade + (5 - grade % 5)
                newGrades.append(new)

    return newGrades

# def gradingStudents(grades):
#     return [ i if (i < 38 or i % 5 < 3) else (i + (5 - i%5)) for i in grades]

