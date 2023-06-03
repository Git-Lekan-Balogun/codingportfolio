# combined.py
with open("numbers1.txt", "w") as f:
    f.write("14 5 2023 5 3 1994")
    # random numbers get written to file (actually today's date and my birthday)

with open("numbers2.txt", "w") as f2:
    f2.write("14 12 1967 3 7 1998 28 2 1997")
    # random numbers get written to file (again, birthdays)

with open("numbers1.txt", "r") as r:
    num1file_contents = r.read()
    # we then read these files, store them into a variable

with open("numbers2.txt", "r") as r2:
    num2file_contents = r2.read()
    # file is read, stored into variable

# we store the read file values into 1 variable


numbers = num1file_contents + " " + num2file_contents
# numbers stores the contents of both files into one variable, we need the space because there is no \n or space at
# end of both files, this will stop our program from joining two numbers together (EOF and SOF numbers, e.g. 13 and 12
# may end up becoming 1312, which of course is a different number

print(numbers)
# 14 5 2023 5 3 1994 14 12 1967 3 7 1998 28 2 1997 = numbers from both files, note that this is a string which affects
# our methods and logic

# TODO: also note that, while it seems plausible or correct to convert the numbers variable into numbers, numbers
#  cannot have spaces, that will make it a string, and we cannot rid the spaces, because this will
#  concatenate the numbers and create a huge one which we dont want

number_elements = numbers.split()
# we can take this string and split it, so that we have our number values as elements in a list, note that currently
# they are still strings

int_values = []
for i in number_elements:
    i = int(i)
    int_values.append(i)
    # we iterate through our list of string numbers, convert each value into it's integer counterpart, and append them
    # into a new list

print(int_values)
# [14, 5, 2023, 5, 3, 1994, 14, 12, 1967, 3, 7, 1998, 28, 2, 1997] = the same values, in a list in their int data form

int_values.sort(reverse=True)
# this method sorts the values, it edits the original list, so we do not need to save this into a new variabele,
# however if we want both the unsorted and sorted versions of this list, we could resave the original list into
# yet another variable, then just use the sort() method on one of these variables

print(int_values)
# [2, 3, 3, 5, 5, 7, 12, 14, 14, 28, 1967, 1994, 1997, 1998, 2023], our numbers in ascending order
# note: we can reverse by adding (reverse=True) as an argument

string_integers = str(int_values)
# we need to convert our list of numbers back into a string so that we can write this into the txt file

with open("numbers3.txt", "w") as w:
    w.write(string_integers)
