# list_types.py

# we're creating a program that demonstrates our understanding of lists:
#
""" Create a new Python file in this folder called list_types.py.
Imagine you want to store the names of three of your friends in a list of
strings. Create a list variable called friends_names, and write the syntax to
store the full names of three of your friends.
Now, write statements to print out the name of the first friend, then the
name of the last friend, and finally the length of the list.
Now, define a list called friends_ages that stores the age of each of your
friends in a corresponding manner, i.e., the first entry of this list is the age of the friend named first in
the other list."""

friends_names = ["Roxana Horvadi", "Kamari Tyce", "Richie Mafwa"]
# storing my friends names in a list
# disclaimer these are random people that I know on instagram

for i in friends_names:
    # i is a variable referring to the current iteration, for the sake of clarity I could named the variable "friend"
    print(i)
    # for each element in the list, print it
print(len(friends_names))
# print the length of the list

friends_ages = ["25", "27", "26"]
# storing my friends ages in the list in respective index order

counter = 0
for i in friends_names:
    print(f"My friend {i} is {friends_ages[counter]} years old.")
    counter += 1

# the task doesn't require us to use string manipulation, however it makes sense to give it a shot

