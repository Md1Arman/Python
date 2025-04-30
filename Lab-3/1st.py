# 1)	Count how many vowels are there in a string. Accept the string from the user.
def check_vovuel(str11):
    check="AEIOUaeiou"
    count=0
    for char in str11:
        if char in check:
            count +=1
    print(count)

str1=input("Enter String:")
check_vovuel(str1)
