# 11)	Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
import math

def coordinate():
    a = int(input("X coordinate: "))
    b = int(input("Y coordinate: "))
    return a, b

print("Enter first coordinate:")
x1, y1 = coordinate()

print("Enter second coordinate:")
x2, y2 = coordinate()

print("Enter third coordinate:")
x3, y3 = coordinate()


d1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
d2 = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
d3 = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)


if abs(d1 + d2 - d3) < 1e-9:  
    print("All three points fall on a straight line")
else:
    print("All three points do not fall on a straight line")
