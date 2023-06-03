# DOB.txt

# for this task we need to demonstrate how to read and write from and to files

"""Write a program that reads the data from the text file called DOB.txt and prints it out in two different sections
in the format displayed below: Name Orville Wright Rogelio Holloway Marjorie Figueroa ...etc Birthdate 21 July 1988
13 September 1988 9 October 1988 ...etc """

with open("DOB.txt", "r") as f:
    # we open the file as "f", and we do not need to f.close() file
    file_contents = f.read()
    # we read the entire contents of f and store it into a variable called file_contents

file_words = file_contents.split()
# here, we're going to store all the words into a variable called file words, from here what we'll do is:
# seeing as we know the files are in sequential order e.g. 1) first name 2) last name 3) day of birth etc
# we will loop over these and string manipulate them so that it displays as required above

first_names_0 = []
last_names_1 = []
day_of_birth_2 = []
month_of_birth_3 = []
year_of_birth_4 = []
# these are going to store the sequential values in the file, that we will use for string manipulation
# i've added the index number as a reference but this is not necessary, just taking advantage of the fact that
# variables can be set to anything

for i, value in enumerate(file_words):
    if i % 5 == 0:  # first names values
        first_names_0.append(value)
    elif i % 5 == 1:  # second names values
        last_names_1.append(value)
    elif i % 5 == 2: # day of birth values
        day_of_birth_2.append(value)
    elif i % 5 == 3:  # month of birth values
        month_of_birth_3.append(value)
    elif i % 5 == 4:  # year of birth values
        year_of_birth_4.append(value)
    else:
        print("Error, exiting program.")
        exit()

counter = 0
print("Name:")
for i in first_names_0:

    # print(f"{first_names_0[counter], last_names_1[counter]}")
    print(f"{first_names_0[counter]} {last_names_1[counter]}")
    counter += 1
    # note:
    # i could set an if statement to reset counter back to 0 if the length of first_names list is met, though I'm not
    # testing efficiency at this level of coding, It would be interesting to run a test to see if manually resetting
    # counter back to 0 or meeting the condition would operate faster, I assume that it would be manually resetting as
    # it's less code to read for the operating system

    # the count counts up, as it increases, we use the counter count to cycle through the index's in each list

print("")
# gives us a space between the two sections
counter = 0
print("Birthdate:")
for i in first_names_0:
    # i'm using first_names_0 here even though we're referring to the dates because the length is the same,
    # however in other occasions this may be a detail worth paying attention to
    print(f"{day_of_birth_2[counter]} {month_of_birth_3[counter]} {year_of_birth_4[counter]}")
    counter += 1

    # as stated before we use the counter count to cycle through the index's in each list
