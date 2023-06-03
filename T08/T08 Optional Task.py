# optional_task1.py
"""This program is going to test whether a number is odd or even."""
users_number = int(input("Enter a number, let's see if it's odd or even: "))
if users_number % 2 == 0:
    print(f"Your number {users_number} is even.")
else:
    print(f"Your number {users_number} is odd.")

print(f"Your number {users_number} when modulo by 2 is {users_number % 2}.")

"""
This program works by using the remainder ability of the modulus function.
if a user enters a number to apply modulus to it by 2, the answer is either 1 or 0.
Even numbers have a remainder of 0, so if it's equal to 0 we can see this is an even number.
Contrary, if it's 1 then it is odd. Our program accepts anything other than 0 as odd."""