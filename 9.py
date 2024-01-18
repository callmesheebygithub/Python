# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not.

def triangle_validity():
    A=float(input("Enter first side point of the triangle: "))
    B=float(input("Enter second side point of the triangle: "))
    C=float(input("Enter third side point of the triangle: "))

    S=(A+B+C)/2

    Area=(S*((S-A)*(S-B)*(S-C)))**0.5

    return Area

Area=triangle_validity()
if Area !=0:
    print("you can formed the triangle")
else:
    print("You can't form the triangle")

# triangle checking by using Angle
    
def triangle_validity():
    A = float(input("Enter first angle of the triangle: "))
    B = float(input("Enter second angle of the triangle: "))
    C = float(input("Enter third angle of the triangle: "))

    # Check if the sum of angles equals 180 degrees (triangle property)
    if A + B + C == 180:
        return True
    else:
        return False

# valid_triangle = triangle_validity()
# if valid_triangle:
#     print("You can form a triangle with these angles.")
# else:
#     print("You can't form a triangle with these angles.")
