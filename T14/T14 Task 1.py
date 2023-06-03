# even.py

"""
We're working with loops and so for this task we're going to enter a number and make
use of the while loop function.
"""

users_num = int(input("Enter a number, we're going to print all even mumbers from 1 up"
                      " to and possibly including your number: \n"))

counter = 0
# while counter < users_num:
#     counter += 1
#     if counter % 2 == 0:
#         print(counter)

"""Because of examples laid out in this exercise, I initiated this while loop block
with the condition within the while function call, we were explained during our 
lectures that this is bad practice, and it did feel a bit alien to me to write
out the statement this way"""
# i believe it's bad practice because sometimes the condition changes for undersirable
# reasons or not as intended

# while True is best practice
while True:
    if counter <= users_num:
        # here if the counter is less than user's number, then continue to add 1 to it
        counter += 1
        if counter % 2 == 0:
            # on the current iteration, if the remainder is 0, it is an even number
            # if it is an even number, print it out
            print(counter)
