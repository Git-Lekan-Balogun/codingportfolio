# finance_calculators.py Capstone 1 - Variables & Control Structures

"""
For this task we create a program that allows the user to calculate their interest on an investment or calculate
the amount that should be repaid on a home loan each month.
"""

import math

users_choice1 = input("Choose an option from the menu:\n"
                      "Investment: \t\t\t [I]\n"
                      "Bond: \t\t\t\t\t [B]\n")
users_choice1 = users_choice1.upper()
# setting up menu screen

if users_choice1 == "I":
    print("")
    deposit_amount = float(input("How much money are you depositing?\n"))
    interest_rate = float(input("What is the interest rate?\n"))
    years_of_invest = float(input("How many years do you plan on investing?\n"))
    interest_type = input("Choose an investment type:\n"
                          "Simple: \t\t\t\t\t [S]\n"
                          "Compound: \t\t\t\t\t [C]\n")
    interest_type = interest_type.upper()
    # setting up investment: simple or compound menu options

    if interest_type == "S":
        returns_amount = deposit_amount * (1 + (interest_rate / 100) * years_of_invest)
        # BIDMAS is important here, it is important that we know what order of operators is taking place
        # BIDMAS = Brackets, Indices, Division, Multiplication, Addition, Subtraction

        print(f"Given that you have a deposit of {deposit_amount} and interest rate of {interest_rate}. With "
              f"{years_of_invest} years of interest under the simple interest type you will have a return of "
              f"{math.trunc(returns_amount)}.")
        # Standard f string displays outcomes to user.

    elif interest_type == "C":
        returns_amount = deposit_amount * math.pow((1 + (interest_rate / 100)), years_of_invest)
        print(f"Given that you have a deposit of {deposit_amount} and interest rate of {interest_rate}. With "
              f"{years_of_invest} years of interest under the compound interest type you will have a return of "
              f"{math.trunc(returns_amount)}.")
        # Standard f string displays outcomes to user.


elif users_choice1 == "B":
    house_value = float(input("What is the current value of the house?\n"))
    interest_rate = float(input("What is the interest rate as a percent?\n"))
    bond_repayment = float(input("How many months do you plan to take on repaying the bond?\n"))

    interest_rate = interest_rate / 100
    # we asked our user to enter the interest rate value as it is as a percentage. If they enter say "7", then to work
    # with this as a percentage is 0.07 like a certain secret agent. Jokes aside, to get this or any percentage we need
    # to divide our given number by 100.

    interest_rate = interest_rate / 12
    # we divide

    monthly_repayment = (interest_rate * house_value) / (1 - (1 + interest_rate) ** (-bond_repayment))

    print(f"Given that the house value is {house_value}, interest rate is {interest_rate} and you stated you will take "
          f"{bond_repayment} months to repay the bond. Your monthly repayments will be £{monthly_repayment}.")
    # Standard f string displays outcomes to user.

    # we are given the formula for the bond repayments. it's the current interest rate * the amount burrowed
    # I believe this gives us the total interest amount divided by the monthly instalments.



else:
    print("You have entered an invalid entry, please restart the application.")

