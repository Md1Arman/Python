def Count_digit(str1):
    count_num=0
    Count_alpha=0
    for char in str1:
        if ord(char)<=57 and ord(char)>=47:
            count_num +=1
        elif ord(char)<=90 and ord(char)>=65 or ord(char)>=97 and ord(char)<=122:
            Count_alpha +=1
    print(f"Number of Digits {count_num} and number of alphabates is {Count_alpha}")

str1=input("Enter String:")
Count_digit(str1)