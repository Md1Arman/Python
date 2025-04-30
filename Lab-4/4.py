# 4)	Check whether a given number is prime, is perfect, is Armstrong, is palindrome, is automorphic.


import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 1:
        return False
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    return sum_divisors == n

def is_armstrong(n):
    num_str = str(n)
    power = len(num_str)
    sum_digits = sum(int(digit) ** power for digit in num_str)
    return sum_digits == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    square = n ** 2
    return str(square).endswith(str(n))

def check_number(n):
    print(f"Number: {n}")
    print("Prime:", "Yes" if is_prime(n) else "No")
    print("Perfect:", "Yes" if is_perfect(n) else "No")
    print("Armstrong:", "Yes" if is_armstrong(n) else "No")
    print("Palindrome:", "Yes" if is_palindrome(n) else "No")
    print("Automorphic:", "Yes" if is_automorphic(n) else "No")


num = int(input("Enter a number: "))


check_number(num)
