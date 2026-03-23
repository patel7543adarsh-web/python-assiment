# Module 5: Files,Exception,and Error in  python
# Task 1: Read a file and Handle Errors
# Problem Statement: Write a python program that:
# 1. Open and read a text file named sample.txt.
# 2. Prints its content line by line.
# 3. Handles error gracefully if the file does not exits.
# Expected Output:
# if the file exits:
# Reading file content:
# Line 1: This is a sample text file.
# Line 2: It contains multiple line.


# if the file does not exits:
# Error: The file 'sample.txt' was not found.

with open ("sample.txt", "w") as file:
    file.write("Line 1: This is a sample text file.\n")
    file.write("Line 2: It contains multiple lines.")
try:
    with open("sample.txt1", "r") as file:
        print("Reading file content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")