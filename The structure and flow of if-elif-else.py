# How does if interact with elif?


num = 16

if num > 12:
    print("the variable num is greater than 12")
    # this condition prints because yes our number is greater than 12, being 16.
elif num > 15:
    print("the variable num is greater than 15")
    # this condition does not print, even though our number is greater than 15, being 16. Because our chain has already
    # been satisfied. In a sense, elif is connected with the first if statement.
    # It is therefore worth noting that order matters, if the information that the number is greater than 12 is more
    # important than the information that our number is greater than 15. Then we're good to go!

if num > 10:
    print("the variable num is greater than 10")
    # A new if statement in the chain resets the checks, so this prints again.
if num > 11:
    print("the variable num is greater than 11")
    # A nested if statement doesn't connect to the previous if just like an elif would. So we find that this also
    # prints. If we had an elif statement after this, that was also true. This elif statement would not print. As it
    # connects to this if statement.

else:
    print("the variable num is 10")

"""
If-else syntax
If (condition is true):
this code activates
Else (if condition is not true):
this code activates

If-elif-else syntax
If (condition is true):
this code activates
Elif (if condition is not true, this condition is true):
this code activates
Elif2 (elif condition not true, this condition is true):
this code activates
Else (all previous if, and elifs are not true):
this code activates

Note:
If elif1 & elif2 are both true. Only elif1 will play out as the code reaches this truth statement and does not execute the rest of the code.
You can avoid this using nested ifs: this will disconnect each if from an elif.

Nested if syntax
If (condition is true)
this code activates
If (condition is (also) true)
this code activates

Note:
Elif is a disconnector and connector. It connects to the if statement above, and disconnect the if statement below.

Elif will end the chain if it’s condition is true.
If will still permit checks in the chain.
"""
