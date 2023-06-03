# full_name.py
"""For this task we'll be validating the fact that a user has entered both a first and a last name.
There would in theory be many parameters to check in this instance, however we are provided the parameters for
what is considered a full name."""
users_name = input("Please enter your full name:\n")
if len(users_name) == 0:
    print("You haven't entered anything. Please enter your full name.")
elif len(users_name) < 4:
    print(f"You have entered only {len(users_name)} characters. Please ensure you have entered both name and surname."
          f"\nIf your names only consists of these characters, please contact admin.")
elif len(users_name) > 25:
    print(f"You have entered {len(users_name)} characters. Please ensure you've only entered your full name.\n"
          f"If your name does in fact consists of these characters, please contact admin.")
else:
    print("Thank you for entering your name.")

"""Here we use the len() feature to count the length of the user's input. As prior stated this is the only parameter
we're using to see if a user has input what is considered to be a full name. However, I've added some realism and
prompted the user to contact the 'admin' given this is a real application."""