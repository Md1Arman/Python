# 4)	Write a function that removes one string from another string, if present. E.g. Onestring = “abcdef”, removestring = “cd”. The finalstring should contain “abef”.
def CheckPresent(str1,str2):
    i=0
    count=0
    index=None
    for char in str1:
        count +=1
        if char==str2[i]:
            index=count
            if i<len(str2)-1:
                i=i+1
            else:
               break 
        else:
            i=0
    num=0
    for ch in str1:
        num+=1
        if(num>index-len(str2) and num<=index):
            continue
        print(ch,end="")

str1=input("Enter String:")
str2=input("Enter String to Check wheather it is in first or not:")

CheckPresent(str1,str2)