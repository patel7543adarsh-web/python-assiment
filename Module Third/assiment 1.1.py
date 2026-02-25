import math 
num = float(input("Enter a number: "))
if num >= 0:
    sqrt_num = math.sqrt(num)
    log_num = math.log(num)
    sine_num = math.sin(num)
    print(f"Square root: {sqrt_num}")
    print(f"Logarithm: {log_num}")
    print(f"Sine: {sine_num}")
else:
    print("Error: The number must be non-negative for square root and logarithm calculation.")