# Task 1: Calaulate factorial using a function
# Problem Statement: Write a python program that:

# 1.Define a function named factorial that takes a number as an argument and calclute its factorial using a loop or recursion
# 2.Return the calculate the factorial
# 3.call the function with a simple number and print the output.
# Expected output:
# For example, if the number is called with 5, it should return:
# Enter a number: 5
# Factorial of 5 is: 120


def factorial(num):
    if num < 0:
        return "factorial is not define for negative number"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range (1, num+1): 
            result *= i
        return result
n = int(input("Enter a number: "))
fact_result = factorial(n)
print(f"factorial of {n} is: {fact_result} ")
