# Optional Task 5
"""This task wants us to convert a data type into another with values that are not convertible. We can't convert
a string into an integer unless the string itself is a number. """
fav_rest = input("Enter your favourite restaurant: ")
int_fav = int(input("Enter your favourite number: "))
print(fav_rest)
print(int_fav)

print(int(fav_rest))