# 5.	A list contains 5 strings. Convert all these strings to uppercase.
def convert_to_uppercase():
    strings = ["hello", "world", "python", "programming", "uppercase"]
    
    upper_strings = [s.upper() for s in strings]

    print("Original List:")
    print(strings)

    print("Uppercase List:")
    print(upper_strings)

convert_to_uppercase()
