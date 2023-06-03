# control.py

users_age = int(input("How many years of age are you? "))
if users_age >= 18:
    print("You're old enough.")
elif 16 <= users_age <= 18:
    print("You're almost there.")
    # this elif condition will simplify itself
    # from elif users_age > 16 and users_age < 18:
    # to elif 16 < users_age < 18:
else:
    print("You're just too young!")

# it is important to thoroughly test all outcomes of our code or enough for it to be sufficient.
# with the following code:

    # users_age = int(input("How many years of age are you? "))
    # if users_age > 18:
    #     print("You're old enough.")
    # elif 16 < users_age < 18:
    #     print("You're almost there.")
    #     # this elif condition will simplify itself
    #     # from elif users_age > 16 and users_age < 18:
    #     # to elif 16 < users_age < 18:
    # else:
    #     print("You're just too young!")

# if we enter 18 we get "You're just too young". This is because the first condition fails, 18 isn't bigger than 18
# Additionally for the second clause 18 is bigger than 16, but again isn't bigger than 18. This condition has an AND
# condition. For an AND condition to be valid, both situations must be true.
# As a result of inputting 18 we therefore get the else outcome. Which states "you're just too young".

# We could probably add 'you're just too young or just 18' but that's a bit too either or!

# We resolve this above block of code by adding the equals operator.

