#If an Employee object contains following details:
#empcode, empname, Date of Joining, Salary
#Write a program to serialize and deserialize this data.
import pickle


class Employee:
    def __init__(self, empcode, empname, date_of_joining, salary):
        self.empcode = empcode
        self.empname = empname
        self.date_of_joining = date_of_joining
        self.salary = salary

    def __str__(self):
        return f"Employee[{self.empcode}, {self.empname}, {self.date_of_joining}, {self.salary}]"


emp = Employee(101, "Aashish", "2023-05-01", 55000)


with open("employee.dat", "wb") as file:
    pickle.dump(emp, file)
    print("Employee object serialized.")

with open("employee.dat", "rb") as file:
    emp_loaded = pickle.load(file)
    print("Deserialized Employee object:")
    print(emp_loaded)

