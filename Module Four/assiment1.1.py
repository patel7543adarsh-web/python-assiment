# Task 2 : Write and Append Data to a File

# problem statement: Write a python program that:
# 1. Take user input and writes it to a file named output.txt.
# 2. Appends additional data to the same file.
# 3. Reads and displays the file content of the file.

# Expected Output:

# Enter text to write to the file: Hellow, Python!
# Data successfully writen to output.txt.
# Enter additional text to append: Learning file handling in python.
# Data successfully append.
# Final content  of output.txt:
# Hellow, Python!
# Learning file handling in python.

file1 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(file1 + "\n")
print("Data successfully written to output.txt.")

file2 = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(file2 + "\n")
print("Data successfully appended.")
print("\nFinal content of output.txt:")


with open("output.txt", "r") as file:
    print(file.read())