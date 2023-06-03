# optional_task2.py
"""This program is going to help the user decide what to wear.
Is the temperature more than 20 degrees?
Is it currently the weekend?
Is it sunny?"""

print("Let us know what the weather's like and we'll suggest you something appropriate to wear.")

while True:
    temperature = input("Is the weather 20 degrees or more?\n")
    temperature = temperature.lower()
    if temperature == "yes":
        print("SPF weather!")
        break
    elif temperature == "no":
        print("Personally I'm cold when the temperatures get below 70.")
        break
    else:
        print("Please enter 'yes' or 'no'.")


while True:
    weekend = input("Is it the weekend?\n")
    weekend = weekend.lower()
    if weekend == "yes":
        print("Have a good break.")
        break
    elif weekend == "no":
        print("On a school day?")
        break
    else:
        print("Please enter 'yes' or 'no'.")


while True:
    sunny = input("Is it sunny outside?\n")
    sunny = sunny.lower()
    if sunny == "yes" and temperature == "no":
        print("Nice.")
        break
    elif sunny == "yes" and temperature == "yes":
        print("Now we're talking!")
        break
    elif sunny == "no" and temperature == "no":
        print("Seems cold.")
        break
    elif sunny == "no" and temperature == "yes":
        print("That's a bit strange!")
        break
    else:
        print("Please enter 'yes' or 'no'.")


if temperature == "yes":
    print("You should wear a short sleeved top..")
else:
    print("You should wear a long sleeved top..")

if weekend == "yes":
    print("..with some shorts..")
else:
    print("..with some jeans..")

if sunny == "yes":
    print("..and a cap!")
else:
    print("..and a raincoat.")

"""So in short, we prompt the user to change some boolean conditions of variables, even going as far as to create
some conditions with two boolean values e.g. if it's sunny but it's not 20 degrees or it's 20 degrees but not sunny
and how that might be strange.

Our program has a particular article of clothing to suggest if a certain boolean value pertaining to a certain aspect
is true or false."""
