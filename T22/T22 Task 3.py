# counting.py

"""● Write a Python program called counting.py to count the number of times a character occurs (character frequency)
in a string. ● Store each letter followed by the number of occurrences in a dictionary and print it out. ● Sample
String : ‘google.com’ ● Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1} """

users_string = list(input("Enter a string and we'll count each character: "))
letter_count = []
# we take the users string, and cast it to a list. this will separate each character
# the letter count is an empty list, that we will use to append each character, but only if it has not been appended
# already

for i in users_string:
    if i not in letter_count:
        letter_count.append(i)
        # appends the current iterable into the list if not already present

tuple_pairs = []
# ??

for i in letter_count:
    coupler = [i, 0]
    coupling = tuple(coupler)
    tuple_pairs.append(coupling)
    # for i in our unique letter list, pair i with 0 (the 0 is going to be the counter for i)
    # next, create a tuple from this pair
    # next, append this tuple into our list of tuples, with this pattern arrangement we can create a dictionary

letter_dict_counter = dict(tuple_pairs)
# cast our list of tuples into a dictionary
# TODO: note that, pycharm doesn't like this, it states that we have a (list(tuple(string-int
#  pycharm wants us to have the following structure (supports key - supports key-value. and numbers as the key value
#  whilst pycharm is upset at my pattern organisation, this is not offensive

for i in users_string:
    # we go back to the users string, it's time to count character occurrence
    if i in users_string:
        # for the current character, if the character is in the string
        letter_dict_counter[i] += 1
        # letter dict counter looks into our dictionary, "i" is our current iteration - a letter
        # when referring to i in the dictionary, we actually refer to its value - which for all characters - will be 0
        # when the character is meant in the loop, we look at that 0 value, and add 1 - so this will add 1 for every
        # occurrence of the char, for each character

print(letter_dict_counter)