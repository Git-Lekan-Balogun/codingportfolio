# disappear.py

# we're making a program that takes in a string from a user, then take in what the user wants removed from the string
# what the user wants removed has to be characters


users_string = "This is an example string."
# our user inputs a string
remover = "ahi"
# our user inputs characters they want to strip from the string

# users_string = input("Enter a string you would like to manipulate:\n")
# remover = input("Enter the characters you would like to strip from the string:\n")
for i in remover:
    # for each character in the string, we take it and remove it from our statement
    # this is repeated for every character in our variable, therefore by the end, all necessary characters are removed
    # from our statement
    users_string = users_string.replace(i, "")

print(users_string)


# users_string = "This is an example string."
# remover = "a"
# print(users_string.replace(remover, ""))

# the above code was my first attempt off the bat, I wanted to test storing a value into a variable, then using that to
# strip then its value from equivalent values in our string
# so if our remover variable was a, my print statement would replace every occurence of "a" with nothing (empty string)
# i then how to figure out, how to repeat this process so that the user can enter multiple characters and these would
# all be stripped from our string

# we can do so with a for loop, which I did

