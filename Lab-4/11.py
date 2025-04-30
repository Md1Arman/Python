# 11)	Calculate sin(x); x is a radian value. The formula is as under:
import math

def sin_taylor_series(x, terms=10):
    sin_x = 0
    for n in range(terms):
        term = ((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1)
        sin_x += term
    return sin_x

x = float(input("Enter the value of x (in radians): "))

sin_approx = sin_taylor_series(x)
sin_actual = math.sin(x)

print(f"sin({x}) using Taylor Series: {sin_approx}")
print(f"sin({x}) using math.sin: {sin_actual}")
