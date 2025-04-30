# 13)	Convert number 0 to 19 to its equivalent words. E.g. 0  zero, 19nineteen.
def number_to_word(n):
    words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
             "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if 0 <= n <= 19:
        return words[n]
    else:
        return "Number out of range. Please enter a number between 0 and 19."


num = int(input("Enter a number (0-19): "))

print("Equivalent word:", number_to_word(num))
