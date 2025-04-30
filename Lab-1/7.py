min=int(input("Enter Minutes Number:"))

print(min,"Minutes is equal to",(min-(min%60))/60,"Hours and",min%60,"Minutes")