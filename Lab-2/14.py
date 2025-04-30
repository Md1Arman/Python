def average():
    math = int(input("Enter Mark in Math: "))
    science = int(input("Enter Mark in Science: "))
    computer = int(input("Enter Mark in Computer: "))

    sum_mark = math + science + computer

    print("Average Mark is", sum_mark / 3)

    print(grade(math), "Math")
    print(grade(science), "Science")
    print(grade(computer), "Computer")

def grade(mark):
    if mark >= 80:
        gra = 'O'
    elif mark >= 70:
        gra = 'A+'
    elif mark >= 60:
        gra = 'A'
    elif mark >= 55:
        gra = 'B+'
    elif mark >= 50:
        gra = 'B'
    elif mark >= 45:
        gra = 'C'
    elif mark >= 40:
        gra = 'P'
    else:
        gra = 'F'

    return gra 

average()
