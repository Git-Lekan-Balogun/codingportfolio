#T04 Optional Task
"""The task for this is to store two numbers in two variables and then swap them around, you of course can't do this
ine one go. The way to do this is to:
store the value of VARIABLE1 into a PLACEHOLDER
reassign VARIABLE1 to VARIABLE2 (variable2 value is in now in variable1)
then reassign VARIABLE2 to PLACEHOLDER, this means placeholder has variable1's value, but it now goes to variable2"""
num1 = input("Please enter a number: ")
num2 = input("Please enter a second number: ")

num_placeholder = num1
num1 = num2
num2 = num_placeholder

print(f"This is your second input '{num1}'.")
print(f"This is the first input '{num2}'.")
