# 2.	Generate 20 random integers and store them in a list. Accept a number from the user and print position of all occurrences of that number in the list.
import random


def find_occurrences():
    numbers = [random.randint(1, 50) for _ in range(20)]
    
  
    print("Generated List:", numbers)
    
    
    target = int(input("Enter a number to find its positions: "))

    
    positions = []
    for index, value in enumerate(numbers):
        if value == target:
            positions.append(index)


   
    if positions:
        print(f"The number {target} is found at positions: {positions}")
    else:
        print(f"The number {target} is not found in the list.")

find_occurrences()
