# task2.py
"""We're creating an app that is used to calculate the area that the foundation of a building covers.
"""
import math

while True:
    building_shape = input("What shape is the building?\n"
                           "Square:\t\t\t\t\t\t [S]\n"
                           "Rectangular:\t\t\t\t [RE]\n"
                           "Round:\t\t\t\t\t\t [RO]\n"
                           "Exit Application:\t\t\t [E]\n")
    building_shape = building_shape.upper()

    if building_shape == "S":
        building_shape_length = float(input("What is the length of the side of the foundation?\n"))
        building_area = building_shape_length ** 2
        print(f"The area of foundation given that it is a square is {building_area}.")
        break
    elif building_shape == "RE":
        building_shape_length = float(input("What is the length of the foundation?\n"))
        building_shape_length2 = float(input("What is the width of the foundation?\n"))
        building_area = building_shape_length * building_shape_length2
        print(f"The area of foundation given that it is a rectangle is {building_area}.")
        break
    elif building_shape == "RO":
        building_shape_length = float(input("What is the length of the radius?\n"))
        building_area = math.pi * (building_shape_length ** 2)
        print(f"The area of foundation given that it is a rectangle is {math.trunc(building_area)} ({building_area}).")
        break
    elif building_shape == "E":
        exit()
    else:
        print("Please enter the valid respective keys.")

"""
Again, simply we have an app that works with inputs we rely on a user to have. Then we make calculations for the user.
They do the easy bit, we do the hard bit.
"""


