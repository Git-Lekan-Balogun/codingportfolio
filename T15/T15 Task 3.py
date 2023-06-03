# task3.py

# For this task we're just exercising our knowledge on loops.
# We will 1) create a while loop that displays a countdown from 20 to 0.
# 2) create a loop that displays all even numbers between 1 and 20.
# 3) a loop that creates increasing asterisks * ** *** **** *****
# 4) create a program that computes the greatest common divisor GCD (the highest common factor)
# of two positive integers.

# 1)
# num = 21
# while True:
#     if num != 0:
#         num -= 1
#         print(num)
#

# 2)
# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)

# 3)
# counter = 0
# for i in range(0, 5):
#     counter += 1
#     print("*" * counter)

# 4)
num1 = float(input("Enter your first number:\n"))
num2 = float(input("Enter your second number:\n"))


# num1 = 3768
# num2 = 1701
# * these are sample numbers

num1_f_string = num1
num2_f_string = num2
# because the values of num1 and num2 change over the course of the code, I want to store their
# original values in these f string versions just so I can display them back in a sentence to the\
# user as you will see later on

if num1 > num2:  # if 3768 is bigger than 1701
    i = num1 % num2  # i = 3768 % 1701 (366)
else:
    i = num2 % num1  # otherwise, modulo num2 by num1 (same result)
    # the importance is that we have the bigger number modulo by the smaller number

# to find this algorithm I used a YouTube video that explains the euclidian algorithm
# source: https://www.youtube.com/watch?v=JUzYl1TYMcU

while True:
    if i == 0:
        # we're going to perform some calculations (the euclidian method), this method
        # involves changing and reassigning the values as though they were actually variables
        # 1) mod the bigger number by the smaller, we get a new value "i"
        # 2) we then mod the previous smaller number by our new smaller number, "i", and from
        # this we will get a new "i" value, repeat until "i" becomes 0

        print(f"Of {num1_f_string} and {num2_f_string} the greatest common divisor is {num2}.")
        break
    else:
        num1 = num2
        num2 = i
        i = num1 % num2
        # the code above is the code for the euclidian algorithm
