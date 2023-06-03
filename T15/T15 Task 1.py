# task1.py
# In this task we learn about for loop and how these are intended for sequences and
# iterables whilst while loops are more so conditional based. As we've covered both loops we also
# delve further and tackle the concept of nested loops.

# Nested loops are simply loops within loops. The concept is as follows: a loop (1) begins and
# within this loop exists another loop (2), loop 2 will finish it's entire cycle or all it's
# iterations before the 2nd iteration of loop 1 begins

# for this task we make a program that allows a user to enter any number, and then they can
# get the multiplication times table for this number up until 12

users_num = int(input("Enter your number and we'll see what it looks like times by each number"
                   "up until 12:\n"))

for i in range(0,13):
    print(f"{i} * {users_num} = {i * users_num}")
