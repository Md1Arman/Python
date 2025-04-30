def Upper_Lower():
    i = 65  
    while i <= 122:  
        if i > 90 and i < 97:  
            i += 1
            continue
        print(chr(i), end="")
        i += 1

Upper_Lower()
