# float_manipulation.py
"""● Create a new Python file in your folder called float_manipulation.py ● You will need to import the math module
and use its built-in functions to complete this task. ● Write a program that starts by asking the user to input 10
floats (these can be a combination of whole numbers and decimals). Store these numbers in a list. ● Find the total of
all the numbers and print the result. ● Find the index of the maximum and print the result. ● Find the index of the
minimum and print the result. ● Calculate the average of the numbers and round off to 2 decimal places. Print the
result. ● Find the median number and print the result. """

import math
import statistics

# users_integers_list = [1, 4, 29.2, 37.2, 11] test code
users_integers_list = []
print("Enter a number, we're looking for 10 floats ideally:")
counter = 0
for i in range(0, 10):
    if counter == 0:
        print(f"You've entered no numbers so far.")
    elif counter == 1:
        print(f"You've entered 1 number.")
    else:
        print(f"You've entered {counter} numbers.")
    users_integers = float(input(""))
    counter += 1
    users_integers_list.append(users_integers)

sum = sum(users_integers_list)
max_index = users_integers_list.index(max(users_integers_list))
min_index = users_integers_list.index(min(users_integers_list))
average = statistics.mean(users_integers_list)
median = statistics.median(users_integers_list)

print(f"The sum of the values you've entered is {sum}.\n"
      f"The biggest number is located at {max_index}, and the smallest at {min_index}.\n"
      f"The average of your values is {average} and your median value is {median}.")
