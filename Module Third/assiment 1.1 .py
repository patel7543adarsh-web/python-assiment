# Task.2 Using the math module for calculation

# Problem Statement: Write a python program that:
# 1. Ask me user for a number as input
# 2. Use the math module to calculate the:
     # square root of a number
     # natural logarithm (log base e) of the number
     # sine of the number in (radian)
# display the calculate the result:
# Expeted output:
# for example, if the user enter 25, the output should be:
     # Enter a number: 25
     # Square root: 5.0
     # logarithm: 3.2188758
     # sine: -0.1323517


import math
def calculate_square_root(num):
    return math.sqrt(num)
def calculate_natural_log(num):
    return math.log(num)
def calculate_sine(num):
    return math.sin(num)


number = float(input("enter a number: "))
print("square root:", calculate_square_root(number))
print("logarithm:", calculate_natural_log(number))
print("sine:", calculate_sine(number))
