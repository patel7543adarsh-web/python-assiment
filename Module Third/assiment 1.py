def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return (x * factorial(x-1))
n = int(input("Enter a number: "))
fact_result = factorial(n)
print(f"factorial of {n} is: {fact_result}")