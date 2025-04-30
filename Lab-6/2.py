# 02. A list contains tuples containing roll no., name and age of student. Write a python program to create three lists separately for roll no., name and age.

def separate_list():
    lst = [(1,'Meetraj',17),(3,'Jainish',18),(9,'Yashvardhan',17),(22,'Abhisek',18),(33,'Meet',18)]
    roll_no = []
    name = []
    age = []

    print(lst)

    for ele in lst:
        roll_no.append(ele[0])
        name.append(ele[1])
        age.append(ele[2])

    print("Roll No =", roll_no)
    print("Name =", name)
    print("Age =", age)

separate_list()
