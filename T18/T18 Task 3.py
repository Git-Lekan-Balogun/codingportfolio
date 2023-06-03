# john.py

# we create a program that will keep prompting for a name, until the correct name is input, then print back
# compilation or list of incorrect entries
"""
● Write a Python program called John.py that takes in a user’s input as a string. ● While the string is not
“John”, add every string entered to a list until “John” is entered. This program basically stores all incorrectly
entered strings in a list where “John” is the only correct string. ● Print out the list of incorrect names. ● Example
program run (what should show up in the Python Console when you run it): Enter your name : <user enters Tim> Enter
your name : <user enters Mark> Enter your name: <user enters John> Incorrect names: [‘Tim’, ‘Mark’] ● HINT: When
testing your While loop, you can make use of .upper() or .lower() to eliminate case sensitivity. """

wrong_entries = []
# our empty list is used to
print("Please enter your name:\n")
while True:
    users_string = input("")
    case_insensitive = users_string.upper()
    if case_insensitive != "JOHN":
        wrong_entries.append(users_string)
    else:
        print(f"Hello John, your list of wrong entries is {wrong_entries}")
