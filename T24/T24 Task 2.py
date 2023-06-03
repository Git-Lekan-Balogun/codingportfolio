# holiday.py

def hotel_cost(x, y):
    return x * y


# this function is to take in a number of nights the user will stay at a hotel for, and the charge per night
# it is interchangeable, but x = nunber of nights, y = price per night

def plane_cost(x):
    x = x.lower()
    if x == "london":
        y = 1000
    elif x == "tokyo":
        y = 2222
    elif x == "stockholm":
        y = 999
    elif x == "lagos":
        y = 4000
    else:
        y = 0
    return y


# this function takes in a city location (x) as a string and returns a price (y), depending on the string (x), function will return a different value for price (y), including none at all


def car_rental(x, y):
    return x * y


# similarly to the hotel, this takes in the number of days for the car rental (x) and the price per day (y)
# note that the task was worded strangely, and only specified to take a number of days and return a price, but didn't state to enter an initial price. for the sake of practicality I will be.

def holiday_cost():
    x = car_rental(float(input("Price of Car Rental:\n")), float(input("How many days renting?\n"))) + plane_cost(
        (input("Destination?\n"))) + hotel_cost(float(input("Price of hotel?\n")), float(input("How many nights?\n")))
    return f"The price of your holiday is {x}"
# x looks into our defined functions: car_rental(), plane_cost(), hotel_cost(), and borrows their functionality
# in our new function holiday_cost, we've set their parameters to user inputs, we are sure to cast the inputs to floats
# because prices can be complex numbers, we are careful to leave our plane_cost() input set to a default or open
# input because we're looking for strings (we could also cast this to str but for the sake of this cast it's redundant)
# we just need to be sure that it isn't also a float or int because this parameter is only looking for a string


print(holiday_cost())
# we don't have a print call in the end of our function, reason being is it does allow for a bit more flexibility
# what if we have a bundle package and want to pair up a few instances of "holiday_cost()"? we may not necessarily
# want ot print out each iteration

"""
price of car rental 100
days renting 5 (500)
destination lagos (4000)
price of hotel 350
nights at hotel 5 (1750)
6250
"""
