# 9)	Print N natural nos. in reverse.
def reverse_natural_numbers(n):
    for i in range(n, 0, -1):
        print(i, end=" ")

N = int(input("Enter a number: "))

if N <= 0:
    print("Please enter a positive number.")
else:
    print(f"First {N} natural numbers in reverse order:")
    reverse_natural_numbers(N)
