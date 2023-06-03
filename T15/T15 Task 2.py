# task2.py

# in this task we're going to create a program to input a year and number of years,
# we will use a for loop to determine and display how many of those years will be leap years


starting_year = int(input("What year would you like to start from?\n"))
number_of_years = int(input("How many years would you like to check?\n"))
number_of_years = number_of_years + 1
# the + 1 is to mitigate the fact that the second argument in range() function is exclusive,
# +1 essentially tricks our program to re add that figure that it excludes

for i in range(0, number_of_years):
    # this is dynamic coding, meaning the code, despite being cemented by one time typing - it
    # moves and is dictated by the current user.

    if starting_year % 4 == 0:
        print(f"The year {starting_year} is a leap year.")
        # leap years are modulo by 4 numbers, this is all the distinction we need for our program
        # to recognise a leap year
    else:
        print(f"The year {starting_year} is not a leap year.")
    starting_year += 1
    # we need to add starting_year to our codeblock, it is not our for loop iteration, but it
    # iterates as we progress through what IS our for loop iteration

# for this task we're given a reference just to help us identify realistically what years are
# actually leap years
# starting year = 1994
# number of years = 8
#  1994 isn't a leap year.
#  1995 isn't a leap year.
#  1996 is a leap year.
#  1997 isn't a leap year.
#  1998 isn't a leap year.
#  1999 isn't a leap year.
#  2000 is a leap year.
#  2001 isn't a leap year.

# a leap year is met every 4 years. so we need to modulo by 4 to establish this distinctive pattern
# if we establish our starting points (starting_year) and our iteration cycles (number of years)
# we can check if a year and the following years will or will not be leap years..