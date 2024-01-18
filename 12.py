# Write a program to find the volume of the cylinder. Also find the cost when ,when the cost of 1litre milk is 40Rs.
import math

def cylinder_volume():
    radius = float(input("Enter Radius of the Cylinder (in cm): "))
    height = float(input("Enter Height of the Cylinder (in cm): "))

    volume = math.pi * (radius ** 2) * height
    return volume

def calculate_milk_cost(volume):
    cost_per_litre = 40
    total_cost = (volume / 1000) * cost_per_litre  # Convert cm³ to litres

    return total_cost

cylinder_volume = cylinder_volume()
milk_cost = calculate_milk_cost(cylinder_volume)

print(f"The volume of the cylinder is: {cylinder_volume:.2f} cubic cm")
print(f"The cost of the milk for this volume is: Rs. {milk_cost:.2f}")

