# manipulation.py

# str_manip = input("Please enter your sentence:\n")
"""This started to get challenging. Printing the length of the string is easy.

Replacing occurrence of the last character with the @ was easy, but my oversight was inputting ".", this meant that the
last character is a period which only occurs once. This made me believe my code did not work. When I removed the period
and left the sentence at the e, all the e's are removed.

print(str_manip[:-4:-1]) is strange because you need to remember that the stop syntax is non-inclusive, it excludes
the actual 4th character itself. Now if you were to print(str_manip[-4]) this is not a slice. It's saying print the
4th most backwards character. It doesn't make sense to 'exclude' anything.

"""

str_manip = "I think we should apologise"
print(len(str_manip))  # printing the length of the string
print(str_manip.replace(f"{str_manip[-1]}", "@"))
print(str_manip[:-4:-1])
print(str_manip[0:3]+str_manip[-2:])
print(str_manip[-4])
