# Write a python program that:
# take an integere from the user.
# Checks whether the number is even or odd using if-else statement
# Display the result according.
# Extended Output:
# The program should return an output like:
# Enter a number: 7
# 7 is an odd number.
# Enter a number: 12
# 12 is an even number.
a = int(input("Enter a number:"))
if a % 2 == 0:
    print(f"{a} is an even number.")
else:
    print(f"{a} is an odd number.")