# 4.	Generate 30 random numbers and put them in a list. Create two more lists – one containing only +ve numbers and another with –ve nos.
import random
def separate_positive_negative():
    numbers = [random.randint(-50, 50) for _ in range(30)]

    print("Original List:")
    print(numbers)

    positive_numbers = [num for num in numbers if num > 0]
    negative_numbers = [num for num in numbers if num < 0]

    print("Positive Numbers List:")
    print(positive_numbers)

    print("Negative Numbers List:")
    print(negative_numbers)

separate_positive_negative()
