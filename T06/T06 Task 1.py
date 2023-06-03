# numbers.py
"""For this task we need the user to enter 3 numbers and our program will perform some complex calculations.
1) Add the numbers added
2) The first number minus the second number
3) The third number multiplied by the first number
4) The numbers added together, then divided by the third"""
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
num3 = int(input("Enter 3rd number: "))

print(f"{num1} + {num2} + {num3} = {num1 + num2 + num3}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num3} * {num1} = {num3 * num1}")
print(f"{num1} + {num2} + {num3} / {num3} = {(num1 + num2 + num3) / num3}")