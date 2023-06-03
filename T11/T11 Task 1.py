# task1.py
"""This looks like a basic exercise to test our understanding of logical operators and how they work.
"""
num1 = 1994
num2 = 29
num3 = 24

# Printing the bigger number.
if num1 > num2:
    print(f"Out of {num1} and {num2}, {num1} is the larger value.")
else:
    print(f"Out of {num1} and {num2}, {num2} is the larger value.")
print()

if num1 % 2 == 0:
    print(f"Your number, num1, {num1} is even.")
else:
    print(f"Your number, num1, {num1} is odd.")
print()

if num1 > num2 and num1 > num3:
    print(f"{num1} is the biggest number.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the biggest number.")
else:
    print(f"{num3} is the biggest number.")

if num2 < num1 < num3 or num3 < num1 < num2:
    print(f"{num1} is the middle number.")
elif num1 < num2 < num3 or num3 < num2 < num1:
    print(f"{num2} is the middle number.")
else:
    print(f"{num3} is the middle number.")

if num1 < num2 and num1 < num3:
    print(f"{num1} is the smallest number.")
elif num2 < num1 and num2 < num3:
    print(f"{num2} is the smallest number.")
else:
    print(f"{num3} is the smallest number.")









