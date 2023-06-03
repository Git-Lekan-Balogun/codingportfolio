# names.py

listed_values = ""
# this is storing a variable as an empty string, we're going to append values from the user until
# they input a 'stop' value

print("Enter the names of the pupils in your class, you can enter 'stop'"
      "once you're finished:")
# this print statement gets separated from the while True block, also the following input
# statement is invisible, so it looks like its actually part of the input function
# the benefit of this is we don't continuously see the prompt to add names reappaear

while True:
    add_names = input("")
    # invisible input, as instructions are above
    if add_names == "stop":
        break
        # if we add this line of code here, it stops our program from actually printing
        # out the word 'stop', because stop is definitely not a student
    listed_values += add_names + "\n"
    # if the input is not "stop", we add the name to list values, this is not a technical list
    # but list in the sense that we're appending values into a variable

print(listed_values)
# the value of "listed_values" has been updated by our loop. it exists outside our loop,
# and so because it wasn't created within the loop it can hold information the loop has made

# while True:
#     add_names = input("")
#     listed_values += add_names + "\n"
#     if add_names == "stop":
#         break
# print(listed_values)

# the above is a previous code attempt where I noticed "stop" was being printed
