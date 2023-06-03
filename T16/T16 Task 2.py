# logic.py
# for this task we simply have to write a program that displays a logical error

users_num = int(input("Enter a number and we'll count up to it: "))
counter = 1

for i in range(0, users_num):
    counter += 1
    print(counter)

# the task prompts us to be a creative as possible, whilst i admit this isn't the most creative I wanted to create a
# logical error, logical errors exist there is no problem with the code during its writing or runtime, however after
# the run time is complete we do not get the desired result or expected result

# this code counts from 2 instead of 1, and counts an extra number to the input by user