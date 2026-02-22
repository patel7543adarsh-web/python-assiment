# Task 1: Calculate Factorial Using a Function
# Problem Statement: Write a Python program that:
# 1.Define a function named factorial that takes a number as an argument and calculate its factorial using a loop or recursion
# 2.Return the calculate factorial.
# 3.Call the function with a sample a number and print output.


# Expeted Output:
# for example, if the function is called with 5, it should return:
# Enter a number: 5
# factorial of 5 is: 120


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