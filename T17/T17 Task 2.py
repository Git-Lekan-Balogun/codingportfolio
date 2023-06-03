# seperation.py

# for this task we need to make a program that prints every word of a string onto a new line

users_string = "This is an example string."
new_line_string = ""
for i in users_string:
    new_line_string += i
    if i == " ":
        new_line_string += '\n'

print(new_line_string)

# this was a simple task, we need to print each word on a new line, each word comes after a space so set our program to
# recognise a space and if there is a space, instread of appending in a space into our empty variable we will append
# a new line