# 12)	Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )

import math

def coordinate(prompt):
    x = float(input(f"Enter {prompt} X coordinate: "))
    y = float(input(f"Enter {prompt} Y coordinate: "))
    return x, y


print("Enter the coordinates of the center of the circle:")
h, k = coordinate("center")

r = float(input("Enter the radius of the circle: "))


print("Enter the coordinates of the point to check:")
x, y = coordinate("point")


distance = math.sqrt(math.pow(x - h, 2) + math.pow(y - k, 2))


if distance < r:
    print("The point lies INSIDE the circle.")
elif distance == r:
    print("The point lies ON the circle.")
else:
    print("The point lies OUTSIDE the circle.")
