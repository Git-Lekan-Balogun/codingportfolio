# task1.py

# for this task we're given a code that has errors and our assignment is to fix the errors
# when doing so, we also need to add a comment in the line and indicate what kind of error it was

# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")
print("\n")
# added parentheses, removed indent (syntax error)

ageStr = 24  #I'm 24 years old.
age = ageStr
print(f"I'm {age} years old.")
three = 3

answerYears = age + three
# removed indent, made ageStr an int value, (syntax error)
# removed int call, as is redundant,
# made ageStr assigned (=) and removed equator (==) (syntax error)
# made print an f string, removed extra speech marks (syntax error)
# made three an int value instead of string value (syntax error)
# removed +'s from print call as this is an f string now (syntax error)

print(f"The total number of years: {answerYears}")
answerMonths = answerYears * 12
print(f"In 3 years and 6 months, I'll be {answerMonths + three + three} months old")


# added parenthesis to both print calls, made print call an f string and removed + (syntax error)
# made answer = answerYears. (syntax error)
# this task was a strange one, it seems the coder made some kind of logical error
# when we fix all the bugs and run the program, our output is 324 months old, however the hint states the coder intends
# a desired result of 330, the coder also makes a random statement "total number of years"
# if we we're working the variables the coder set, we add 2 + three's to get the desired outcome (logical error)

#HINT, 330 months is the correct answer


"""
reference:

print "Welcome to the error program"
    print "\n"

    ageStr == "24 years old" #I'm 24 years old.
    age = int(ageStr)
    print("I'm" + age + "years old.")
    three = "3"

    answerYears = age + three

print "The total number of years:" + "answerYears"
answerMonths = answer * 12
print "In 3 years and 6 months, I'll be " + answerMonths + " months old"

#HINT, 330 months is the correct answer
"""