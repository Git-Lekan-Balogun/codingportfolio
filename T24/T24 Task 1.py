# my_function.py

# this task will test our understanding of user defined functions

def weekdays():
    # def keyword, no parameters because we don't need to work with anything the user or myself may input
    return print("Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.")
    # return and store this value into the call of the function, i've included print in the return statement so that
    # we don't have to call it each time


weekdays()
# prints each day of the week, the task doesn't specify how dynamic this has to be

# we need to create a function that takes a string and replaces each other word with "hello"
def hello_again(x):
    # our function is called "hello_again" (which is kind of a play on words)
    counter = 0
    # our counter is used to dynamically iterate through our string, each loop it will increment, and we will use this to target every word
    a = x.split()
    # to target every word, we will split using the "space" as a delimiter
    b = ""
    # once we have our words in a list, we need to get them back into a string, this "b" value will hold an empty string ready to += our elements (words) back into
    for i in a:
        if counter % 2 == 0:
            i = "hello"
        # for each element, if the counter modulo by 2 is 0, this means its either a word, or the "each other" word, if its each other word, change the value of the element or word to "hello"

        b += i + " "
        # append these values back into our empty string
        counter += 1
        # increment our counter so that we're consistently targeting every other word
    return b


my_sentence = "Hi my name is Lekan Balogun"
print(hello_again(my_sentence))
