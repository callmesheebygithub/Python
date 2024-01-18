# Write a program to find the euclidean distance between two coordinates.

import math

def euclidean_distance():
    x1 = float(input("Enter x1: "))
    x2 = float(input("Enter x2: "))
    y1 = float(input("Enter y1: "))
    y2 = float(input("Enter y2: "))

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    return distance

distance = euclidean_distance()
print(f"The Euclidean distance between the points is: {distance:.2f}")
