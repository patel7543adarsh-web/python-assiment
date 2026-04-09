# Task 2: Sum of integer from 1 to 50.
# Write a python program that:
# 1.Uses a for loop to iterate over number from 1 to 50.
# 2.Calculate the sum of all integer in this range.
# 3.Display the final sum.
# Extended output:
# The sum of number from 1 to 50 is: 1275
sum = 0
for number in range (1,51):
    sum += number
    print(f"The sum of number from 1 to 50 is:{sum}")
