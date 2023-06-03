# whilst i was coding my capstone project for the first time, one of the challenges I faced was keeping track of the
# flow of control along my program both in the figurative sense and the literal sense, the literal referring to how confusing
# things became trying to keep indented blocks in order.

# one way I overcame this was segmented my code blocks by coding them into a second file such as this
# we later learned the def method which allows us to stay true to DRY (Don't repeat yourself)
# the def function or method allows you to write a block of code that you would likely repeat in your code, and
# summarise it into a short line so that this code block can be referred to again
#
# whilst I can go out of my way to apply this, for this capstone I will simply copy over code blocks as by this point
# in the course DRY and def method has not been taught.

# this .py file will consist of codeblocks that would otherwise be defined as functions

# try again block
# if the user has failed; prompt the option for a second try
# y = yes, user wishes to attempt again
# n = no, user wishes to give up and quit
# etc = the user doesn't enter the above respective values

# while True:
#     retry = input("Try again?\n"
#                   "Yes:\t\t\t [Y]\n"
#                   "No:\t\t\t\t [N]\n").lower()
#     if retry == "y":
#         break
#     elif retry == "n":
#         print("Exiting application")
#         exit()
#     else:
#         print("You have entered an incorrect value.\n")
#         continue

print(7 % 6)