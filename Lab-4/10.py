# 10)	Generate N numbers of Fibonacci series
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b

N = int(input("Enter the number of terms: "))

if N <= 0:
    print("Please enter a positive number.")
else:
    print(f"First {N} Fibonacci numbers:")
    fibonacci_iterative(N)
