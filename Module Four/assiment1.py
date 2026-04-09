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

def a_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for i, line in enumerate(file, start=1):
                print(f"{line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Call the function
a_file("sample.txt")