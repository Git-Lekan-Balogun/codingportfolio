# bmi_task.py
"""We're creating a program that calculates a person's BMI."""
import math

users_weight = float(input("Please enter your weight (KG): \n"))
users_height = float(input("Please enter your height (M): \n"))

bmi = users_weight / ((users_height) * (users_height))

print(f"Your BMI is calculated at {bmi}.\n"
      f"The BMI chart is as follows:\n"
      f"If your BMI is 30 or greater, it is in this regard you are considered 'obese'.\n"
      f"If your BMI is 25 or greater, it is in this regard you are considered 'overweight'.\n"
      f"If your BMI is 18.5 or greater, it is in this regard you are considered 'standard'.\n"
      f"If your BMI is less than 18.5 it is in this regard you are considered 'underweight'.\n")

if bmi >= 30:
    print(f"As your BMI is {math.trunc(bmi)} it is with this regard you are considered 'obese'.")
elif bmi >= 25:
    print(f"As your BMI is {math.trunc(bmi)} it is with this regard you are considered 'overweight'.")
elif bmi >= 18.5:
    print(f"As your BMI is {math.trunc(bmi)} it is with this regard you are considered 'standard'.")
elif bmi < 18.5:
    print(f"As your BMI is {math.trunc(bmi)} it is with this regard you are considered 'underweight'.")
else:
    print("Program error.")

"""
To make this BMI calculator we get some inputs from the user to work with. 
Perform some calculations with a formula to calculate the user's BMI.
Given the result of the calculation, our program will print one statement or another. 
These statements will let the user know what they're considered with regard to BMI.

Note:
The ethics of such an application may be outdated, to mitigate I put the words obese, overweight,
standard (which throughout the exercise is referred to as normal, and underweight.
This exercise is simply to demonstrate the logic and understanding of how such an application would
function. 

I am aware that someone may have, for example an extremely high number for their BMI given their
height and their weight. However in reality be extremely healthy. Or that to be overweight or
underweight may not always imply that one is unhealthy. Thought it may be (at times) an indicator.
"""