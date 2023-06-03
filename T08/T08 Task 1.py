# baby.py
"""We're making a program that is used to see if a user is 18 or older and allowed entry into a party."""
current_year = int(input("Please enter the current year: "))
user_dob = int(input("Please enter year of birth: "))
if current_year - user_dob < 18:
    print(f"Looks like you're too young, seeing as you're {current_year - user_dob}. Sorry.")
else:
    print(f"Looks like you're old enough. If you're {current_year - user_dob} then you must be familiar "
          f"with the 18+ gang.\nWelcome!")

"""This code takes in the user's year of birth and the current year.
If we deduct the user's year of birth from the current year we'll be left with the users age.
If that user's age is less than 18, the're not allowed in.
Otherwise they are. Welcome!"""