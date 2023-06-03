# task4.py

"""This task we will be establishing characteristics about the user's input number.
Namely, that it's divisible by 2 and 5,
divisible by 2 or 5
or not divisible by 2 or 5."""

users_input = int(input("Please enter your number: "))
if users_input % 5 == 0 and users_input % 2 == 0:
    print(f"Your number {users_input}, is divisible by 2 and 5.")
elif users_input % 5 == 0 or users_input % 2 == 0:
    print(f"Your number {users_input}, is divisible by 2 or 5.")
    if users_input % 5 == 0:
        print("Namely 5.")
    else:
        print("Namely 2.")
elif users_input % 5 != 0 or users_input % 2 != 0:
    print(f"Your number {users_input}, is not divisible by 2 or 5.")

"""
If a number is divided by {your number} and leaves a remainder of 0, then that number is whole divisible 
by your {your number}.
If we set up conditions to check if its 1) divisible by both 2 and 5, divisible by 2 or 5 not divisible by 2
or 5 (not or = and) then the rest is history.
"""


