
# 9.	Take two lists of numbers. Create third list of numbers for only those numbers from first list which are not there in 2nd list (use list comprehension). 


def difference_list(list1, list2):
    result = [num for num in list1 if num not in list2]
    return result

list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = [3, 6, 8, 10, 12]

list3 = difference_list(list1, list2)

print("First List:", list1)
print("Second List:", list2)
print("Third List (Numbers from first list not in second list):", list3)
