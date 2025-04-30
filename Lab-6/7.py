
my_tuple = (10, 20, 30, 40, 50)

temp_list = list(my_tuple)

del temp_list[2]

my_tuple = tuple(temp_list)

print("Updated tuple:", my_tuple)
