# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.


animal = "Lion"
animal_type = "Cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"

print(full_spec)

# added parentheses lines 12 (syntax error)
# added speech marks to Lion and made cub a capital C lines 7, 8
# added f to make full spec an f string, and print its value appropriately lines 11
# switched number of teeth with animal type so that the value reads correctly lines 11


"""reference:
animal = Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = "This is a {animal}. It is a {number_of_teeth} and it has {animal_type} teeth"

print full_spec"""