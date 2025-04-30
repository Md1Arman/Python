# 3.	Generate 50 random numbers in the range 1 and 30. Remove all duplicate values from the list.
import random

def unique_random_numbers():
    numbers = [random.randint(1, 30) for _ in range(50)]
    
    print(numbers)
    unique_numbers = list(set(numbers))
    print(unique_numbers)

unique_random_numbers()
