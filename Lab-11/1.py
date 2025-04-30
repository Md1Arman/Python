# 01. Write a program that receives an integer an input. If a string is entered instead of an integer, then report an error and give another chance to user to enter an integer. Continue this process till correct input is supplied.

def Exc():  
    try:
        a = int(input("Enter an integer: "))
    except Exception:
        print("Please Enter Integer")
        intinput()
    else:
        print("runing")

EXc()        