# alternative.py

# we're starting to learn about string manipulation. String manipulation is used so that we can derive data and results
# from raw data, for example we might open a file and extract a sequence of numbers that relate to some other characters
# in another file, using string manipulation we pair the raw data up and derive the quality information

# in this task we need to make character's in a user's input alternate between capital and lowercase

users_string = "This is an example string"
# users_string = input("Enter a string you'd like manipulated:\n")
# stored example string into users_string instead of input because it's faster to test

counter = 0
users_new_string = ""
# counter is here to + 1 through each iteration of the user's string, the length of iteration is determined by the
# for loop and so will be as long as the users input
# user's new string is empty but will be used to store the new content
for i in users_string:
    # for the current iteration in the user's string
    counter += 1
    # add 1 to counter to increase the count
    if counter % 2 == 0:
        # if the counter fulfils this condition, (every other iteration)
        i = i.upper()
        # the value of i is now it's self in the capital form
        users_new_string += i
        # add this value to the empty string
    else:
        i = i.lower()
        # if it doesn't fulfil the condition, (every other iteration), the value will be forced into it's lowercase
        # version
        users_new_string += i
        # then added to the new string
        
print(users_new_string)


# This took me a bit of trial and error as I've forgotten to how to refer to the index number value of a string
# looping through this code, i wanted to get access to the index number e.g. 2 and not it's value e.g. 'i'

# because i could not access the index number, and instead were accessing it's value, I created the counter

# at this point I may have to venture back into my old task submission*
#
# * (reminding you that this is a second run through)of the course with illustrations to demonstrate knowledge and
# understanding
