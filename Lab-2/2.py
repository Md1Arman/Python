a=int(input("Enter number:"))
b=int(input("Enter number:"))
c=int(input("Enter number:"))




if a>b:
    if a>c:
        if b>c:
            print(c,"is smaller")
        else:
            print(b,"is smaller")
        print(a,"is grester")
    else:
        print(c,"is grester")
        print(b,"is smaller")

elif b>a:
    if b>c:
        if a>c:
            print(c,"is smaller")
        else:
            print(a,"is smaller")
        print(b,"is grester")
    else:
        print(c,"is grester")
        print(b,"is smaller")



