import math

def permutation(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


n = int(input("Enter value of n: "))
r = int(input("Enter value of r: "))


if r > n or n < 0 or r < 0:
    print("Invalid input! r should be less than or equal to n and both should be non-negative.")
else:
    print(f"nPr ({n}P{r}) = {permutation(n, r)}")
    print(f"nCr ({n}C{r}) = {combination(n, r)}")
