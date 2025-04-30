# 8)	Print factorial of a given number.

import math

def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    return math.factorial(n)

num = int(input("Enter a number: "))

print(f"Factorial of {num} is {factorial(num)}")
