# 2)	Write your own functions (without using built-in functions) to convert all characters of a string into lower case/upper case/toggle case.
def ToLower(str1):
    char=''
    for char in str1:
        if 'A'<=char and 'Z'>=char:
            char=chr(ord(char)+32)
        print(char,end="")

def ToUpper(str1):
    char=''
    for char in str1:
        if 'a'<=char and 'z'>=char:
            char=chr(ord(char)-32)
        print(char,end="")


def Toggle(str1):
    for char in str1:
        if 'A'<=char and 'Z'>=char:
            print(chr(ord(char)+32),end='')
        elif 'a'<=char and 'z'>=char:
            print(chr(ord(char)-32),end="")
        else:
            print(char,end="")


str1=input("Enter String:")
choise=int(input("Enter 1 to convert to lowercase. 2 for upper case. 3 to toggle: "))

if(choise==1):
    ToLower(str1)
elif(choise==2):
    ToUpper(str1)
else:
    Toggle(str1)
