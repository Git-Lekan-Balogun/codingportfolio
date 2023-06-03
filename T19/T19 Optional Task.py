# optional_task.py

# goal of this task is to write a program that reads a text file and lets you know:
# the character count
# the word count
# the line count.

# I enjoyed this task and thoroughly enjoyed this second go through of the task

with open("input.txt", "r") as f:
    # here i open the file as "f", f is python's in code representation of the file's data, f is a variable
    file_contents = f.read()
    # i use .read() to read the entire file into "file_contents" variable for later use
    f.seek(0)
    # we use seek to reset the cursor for the file
    file_contents2 = f.readlines()
    # with readlines this will read and store each line of the file into a list (oddly it saves the escape character
    # too) readline in comparison does it for a line at a time
    # using this, if we count readlines we count the items in a list


len_of_file = len(file_contents)
# here is the first use of our file variable, bear in mind that .read() reads all the individual characters in the file
# we know this because the argument specifies how many characters to read, note: when we count particular values, we
# will also use this variable because of the way it has interpreted the data
# read() = char manipulation

word_count = file_contents.split()
# though file_contents is char manipulation, we can target groups of these chars. we know that typically a group of
# chars between two spaces is an actual word, we can use the .split() method to isolate these groups, then count the
# length of these, this would be our word count
# read() + split = word identification

line_count = len(file_contents2)
# line count is interesting, i'm sure we can enter code that recognises the "\n" character and everytime this character
# is present, consider there to be a new line
# i also know that

a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0
# counts the value

for i in file_contents:
    if i == "a":
        a_count += 1
    elif i == "e":
        e_count += 1
    elif i == "i":
        i_count += 1
    elif i == "o":
        o_count += 1
    elif i == "u":
        u_count += 1
    # character checker, counts values when certain values are met/matched

print(f"The character count of the file is {len_of_file}.\n"
      f"The word count of the file is {len(word_count)}.\n"
      f"The line count of the file is {line_count}.\n"
      f"Regarding the vowels: \n"
      f"A:\t\t\t{a_count}\n"
      f"E:\t\t\t{e_count}\n"
      f"I:\t\t\t{i_count}\n"
      f"O:\t\t\t{o_count}\n"
      f"U:\t\t\t{u_count}\n")

# reference: input.txt consists of lyrics from Law of Recognition

"""
*psuedocode/ notes
to get numbers, i think we will use read() and do something with the argument passed into read
we might try to for i in read() variable, this should give us a character count
or print(len(read-variable)

to get words, we read all into a variable, split by space delimiter, then count items in the list
to get lines we will read lines and count the loops

to get vowel count, we will work with the first instruction but if statement set to a e i o u, if it is these, count
the total values, and for shits n giggles well count each individual letter
"""
