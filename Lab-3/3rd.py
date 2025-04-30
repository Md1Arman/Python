# 3)	Accept two strings. Check whether one string is there in another string.
def CheckPresent(str1,str2):
    i=0
    count=0
    for char in str1:
        if char==str2[i]:
            if i<len(str2)-1:
                i=i+1
                count=1
            else:
               break 
        else:
            count=0
            i=0
    if count==1:
        print(f"{str2} is Present in {str1}")
    else:
       print(f"{str2} is not Present in {str1}")

str1=input("Enter String:")
str2=input("Enter String to Check wheather it is in first or not:")

CheckPresent(str1,str2)