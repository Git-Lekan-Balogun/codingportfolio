# student_register.py

# for this task, we're creating a program that allows students to register for an exam
"""● We will write a program called student_register.py that allows students to register for an exam venue. ● First,
ask the user how many students are registering. ● Create a for loop that runs for that amount of students ● Each time
the loop runs it needs to ask the next student to enter their ID number. ● Write each of the ID numbers to a Text
File called reg_form.txt ● Include a dotted line to sign because this document will be used as an attendance register
which the students will sign when they arrive at the exam venue. """

student_amount = int(input("How many students are registering?\n"))
# dynamic input decides loop count
student_register = ""
# empty string value used to append user input values

for i in range(0, student_amount):
    # loop count determined by earlier user input
    print(f"Registered Students: {i}")
    # the above is just a visual counter to help the user keep track of their current iteration
    student_name = input("Enter student's name: ")
    # we use this to continue aiding user's visual aid, storing the current student's name into a value allows us to
    # ask the user what that *students name*'s id is, instead of stating "enter student ID", it's helpful because if
    # the user afks, then returns to desk, they can see what iteration they're on, "Enter Student ID" is ambiguous,
    # user would possibly have to restart application if they forget their current iteration
    student_register += f"Student Name: " + student_name + ", " + "Student ID: " + \
                        input(f"Enter {student_name}'s ID number: ") + \
                        " Student Signature: ...............................................\n"
    # the above string structure is being stored, also appended into the student_register variable,

with open("reg_form.txt", "w") as register:
    register.write(f"{student_register}")
    # this code block writes that string value into the txt document

print(f"Written to file: \n{student_register}")
# this improves user experience, confirming to the user that the txt value has been written to file
# it is important that this code comes after the code that writes to file, because it is possible in theory for
# the current code block to fail, which means if this code block was above and ran, the actual code that writes the txt
# could still fail - and this would be problematic for the user
