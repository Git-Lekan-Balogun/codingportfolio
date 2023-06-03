# =====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

# ====Login Section====
with open("user.txt", "r") as user_database:
    user_database_string = user_database.read()
    # reading the user txt file, this txt file represents the user database, we're storing it into a variable called
    # user_database_string, I'm aware that we will have a lot of variables in this project, so it is vital that our
    # variables are easy to keep a track of and are labelled pragmatically

user_database_list = user_database_string.split()
# exiting our file code block, we want some variables to be globally accessible or in other words have a wide range
# of scope

tasklines = []
# tasklines was added retrospectively, after about 400 lines of code, this will be used to accept a line which is
# compiled of all the details of a single task, this was needed for "vm" menu where we need to identify the user
# and display the tasks that belong to that user, if that user is logged in
# an alternative to this would be to create a dictionary

print(f"user_database_string: {user_database_string}")
print(f"user_database_list: {user_database_list}")
# for the sake of testing, we're just having our values printed out to us

while True:
    user_username = input("Enter your username: \n")
    # we need our user input commands inside of loops so that each iteration the user can be tried again

    if (user_username + ",") in user_database_list:  # 1 (I am using numbers as breadcrumbs to keep track of my loops)
        # user_username + "," puts the comma in the file against the users input, we don't expect the user to enter
        # this value, but we also don't want to remove it

        username_index = user_database_list.index(user_username + ",")
        # username_index stores the value of the index that the user input, our file is set up so that if a username
        # is located at index 1, its respective password will be at index 2

        user_password = input("Please enter your password: \n")
        if user_password == user_database_list[username_index + 1] and user_username == "admin":  # 1.1
            # again our file is set up so that "index0" is username and respective "index1" is index 1 username's pass
            # for any given username located at an even index, its respective password will be at the next odd index
            # the code here treats our database list like a makeshift dictionary
            print("Administrator login successful!")
            print(f"Hello, {user_username}.")

            # TODO: ADMIN MENU
            while True:
                # presenting the menu to the user and
                # making sure that the user input is converted to lower case.

                user_choice = input(
                    "Select one of the following options:\n"  # we're being taken back to this while True
                    "Register a user:\t\t\t\t\t\t[R]\n"
                    "Add a task:\t\t\t\t\t\t\t\t[A]\n"
                    "View all tasks:\t\t\t\t\t\t\t[VA]\n"
                    "View my tasks:\t\t\t\t\t\t\t[VM]\n"
                    "Display statistics:\t\t\t\t\t\t[DS]\n"
                    "Exit:\t\t\t\t\t\t\t\t\t[E]\n").lower()
                # this is our menu, we display a string showing the user what keys match up with what options,
                # we've also forced user's entry into their lower case so that our program isn't case-sensitive

                if user_choice == "r":
                    print("Registering a new user..")
                    while True:
                        new_username = input("Enter the new user's username: \n")
                        # we store this to later write into the database
                        if (new_username + ",") in user_database_list:
                            print(f"The username '{new_username}' already exists, please enter a different username.")
                            continue
                            # we don't want duplicate usernames, if we coded with a dictionary we could avoid this issue
                            # since we haven't, we need a line of code to prevent this from happening, as this would
                            # confuse our previous lines of code

                        new_password = input("Enter the new user's password: \n")
                        # we store this to later write into the database
                        password_confirmation = input("Enter the new user's password again to confirm the new user's "
                                                      "password: \n")
                        # this improves user experiences, if they've entered their password correctly twice, chances are
                        # this is definitely the password they intend to use
                        if new_password == password_confirmation:
                            # if the password match, let's continue
                            with open("user.txt", "a+") as user_database:
                                user_database.write(f"\n{new_username}, {new_password}")
                                # we reopen the file, and we're writing a new line with the username", " user's password
                            print(f"User {new_username} has been created and written to database.")
                            # the confirmation gets read back to user
                            break
                            # this will loop, but once we get this far let's return to the menu

                        elif new_password != password_confirmation:
                            print("The two passwords do not match.")

                            retry = input("Try again?\n"
                                          "Yes:\t\t\t [Y]\n"
                                          "No:\t\t\t\t [N]\n"
                                          "Exit:\t\t\t [E]\n").lower()

                            # if the passwords don't match, we should let the user attempt again, but let's also give
                            # them the option, they may just have a change of mind
                            if retry == "y":
                                print("Please try again..")
                                # this works like an end of loop, bringing us back to the user entering the new user
                            elif retry == "e":
                                print("Exiting application.")
                                exit()
                                # if the user enters no, they quit the application
                            elif retry == "n":
                                print("Returning to main menu..")
                                break
                                # this will return to menu
                            else:
                                print("You have entered an incorrect value.\n")
                                continue  # starts this loop again

                elif user_choice == "a":
                    '''In this block you will put code that will allow a user to add a new task to task.txt file
                    - You can follow these steps:
                        - Prompt a user for the following: 
                            - A username of the person whom the task is assigned to,
                            - A title of a task,
                            - A description of the task and 
                            - the due date of the task.
                        - Then get the current date.
                        - Add the data to the file task.txt and
                        - You must remember to include the 'No' to indicate if the task is complete.'''

                    while True:
                        # we begin with while True, because if the user fails we want them to keep trying until
                        # otherwise, or quit
                        assigned_user = input("Which user is this task assigned to?\n")
                        assigned_user = assigned_user + ","
                        if assigned_user in user_database_list:
                            assigned_user_index = user_database_list.index(assigned_user)
                            # who is the task assigned to? if the value exists, we can proceed, however furthermore
                            # because we're using a list, what if the "username" is actually someone's password? the
                            # pass would exist, but it is not a username. we know that passwords are only at odd
                            # indexes, so let's ensure that the "username" is not located at an odd index
                            if assigned_user in user_database_list and assigned_user_index % 2 == 0:
                                pass
                                # if the assigned user is in the database, and at an even index, continue

                        elif assigned_user not in user_database_list:
                            print("The user does not exist, please create user or try again.")
                            # if the value is not in the list, prompt user to retry
                            retry = input("Try again?\n"
                                          "Yes:\t\t\t [Y]\n"
                                          "No:\t\t\t\t [N]\n"
                                          "Quit:\t\t\t [Q]\n").lower()
                            if retry == "y":
                                continue
                                # allows user to attempt again
                            elif retry == "n":
                                break
                                # allows user to return to menu
                            elif retry == "q":
                                print("Exiting application")
                                exit()
                                # allows user to exit application
                            else:
                                print("You have entered an incorrect value.\n")
                                # loops user as they have entered bad input

                        task_title = input("What is the title of the task?\n")
                        task_title = task_title.replace(",", "")
                        # the name of the task is stored in a variable, note that we re-save their input - because
                        # the nature of our database, commas interrupt our application's interpretation of the database
                        # we will repeat this for each applicable value

                        task_description = input("What is the task description?\n")
                        task_description = task_description.replace(",", "")
                        # user describes the task

                        task_due_day = int(input("Task Due (Day):\n"))
                        task_due_month = int(input("Task Due (Month):\n"))
                        task_due_year = int(input("Task Due (Year):\n"))
                        # user enters integer values that make up the date

                        task_due_date = datetime.date(task_due_year, task_due_month, task_due_day)
                        task_due_date = task_due_date.strftime("%d,%b,%Y")
                        # we have imported a date/time module that allows us to fuse mathematical logic and apply it
                        # with the structure of dates, we have our integer values that represent a respective date,
                        # the date module converts this into a date object
                        # in addition, we then convert this into a string that can be written to task database, in the
                        # same format as the example dates that already exist
                        # the strftime("%d,%b,%Y") values are conversion values,
                        # %d = numbered day, 1-31
                        # %b = short formed month, Jan-Dec
                        # %Y = full form century, 0-9999

                        # TODO: note, retrospectively I am of the fact that I can convert these values with out the
                        #  the commas, however at the time of coding I was under the impression that I had to further
                        #  manipulate the converted string to thus remove the commas

                        task_due_date = task_due_date.replace(",", " ")
                        # the converted string produces commas, so we manipulate the string to remove them
                        current_time = datetime.datetime.today()
                        # probably my favourite feature of the datetime module, the ability to work with the micro
                        # second that you run the program, the task assigned feature is set to the current time the user
                        # sets the task

                        task_assigned_date = current_time.strftime("%d,%b,%Y")
                        # we need the assigned date in the same format we have the due date,
                        task_assigned_date = task_assigned_date.replace(",", " ")
                        # we manipulate the converted date string

                        task_status = "No"
                        # all tasks have a status, as the task is set this status is set automatically to No, as the
                        # task won't be complete when it's just being set. in later menu option we will have a chance
                        # to change the status

                        taskline = (f"\n{assigned_user} {task_title}, {task_description}, "
                                    f"{task_assigned_date}, {task_due_date}, {task_status}")

                        # the line that the user has created through their inputs is formed and stored in a variable
                        # note that it begins with \n, we want to ensure that this is on a new line
                        # note that assigned user has no comma following its value - this is because we actually work
                        # with the username's value and the comma, the comma is in a way already there
                        # the alternative to this would be reverting the value back to the value without the comma, or
                        # storing the two values into two different variables

                        with open("tasks.txt", "a+") as task_database:
                            task_database.write(taskline)
                            # we write this to our task database
                            # this is in append mode, so the task will be added to the end of the file

                elif user_choice == "va":
                    pass
                    '''In this block you will put code so that the program will read the task from task.txt file and
                     print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
                     You can do it in this way:
                        - Read a line from the file.
                        - Split that line where there is comma and space.
                        - Then print the results in the format shown in the Output 2 
                        - It is much easier to read a file using a for loop.'''

                    with open("tasks.txt", "r") as task_database:
                        all_tasks = task_database.read()
                        # opening the file to read its contents into a variable

                    all_tasks = all_tasks.replace("\n", ", ")
                    # when we read the file, there are escape characters, these escape characters are understood as to
                    # us as spaces, but by the computer as "\n", ultimately we need to treat this as ", " because
                    # that's how we want to segment our sentences that form 1 given task

                    # e.g.
                    # task_user, task_name, task_descript\n
                    # task_user2, task_name2, task_descript2\n becomes
                    # task_user, task_name, task_descrip, task_user2, task_name2, task_descript,

                    tasks_formatted = all_tasks.split(", ")
                    # splitting by the ", " *comma space
                    # these are the values we need, these values are sequential. so we know that every 0th/6th value is
                    # going to be the user's name, every 1st and 7th value is going to be a task name

                    structure_user = []  # 0, 6..
                    structure_taskname = []  # 1, 7 etc..
                    structure_task_description = []  # 2
                    structure_assigned_date = []  # 3
                    structure_due_date = []  # 4
                    structure_task_status = []  # 5

                    for i, value in enumerate(tasks_formatted):
                        if i % 6 == 0:
                            structure_user.append(value)
                        if i % 6 == 1:
                            structure_taskname.append(value)
                        if i % 6 == 2:
                            structure_task_description.append(value)
                        if i % 6 == 3:
                            structure_assigned_date.append(value)
                        if i % 6 == 4:
                            structure_due_date.append(value)
                        if i % 6 == 5:
                            structure_task_status.append(value)

                        # enumerate allows us to work with the index and the index value
                        # if we modulo the index by the total number of detail in sequence, the outcome/remainder is the
                        # index of the value

                        # in other words, the first value is a username, the username is at index 0
                        # in a taskline, there are 6 details, if we modulo 0 by 6 we will get 0, this is the username
                        # if we modulo 1 by 6, we'll get 1, and if we increment e.g. 2 by 6 will get 2

                    counter = 0
                    # counter is used to give a task a corresponding task number
                    for i in range(0, len(structure_user)):
                        # it is okay to use structure_user to iterate, as there should be as much "users" as there are
                        # tasks lines
                        counter += 1
                        # task 1 should start at 1, humans don't count like computers
                        print(f"Task #:\t\t\t\t\t\t\t\t {counter}")
                        print(f"Assigned user:\t\t\t\t\t\t {structure_user[i]}\n"
                              f"Task name:\t\t\t\t\t\t\t {structure_taskname[i]}\n"
                              f"Task description:\t\t\t\t\t {structure_task_description[i]}\n"
                              f"Date assigned:\t\t\t\t\t\t {structure_assigned_date[i]}\n"
                              f"Date due:\t\t\t\t\t\t\t {structure_due_date[i]}\n"
                              f"Task Complete:\t\t\t\t\t\t {structure_task_status[i]}\n")

                elif user_choice == "vm":
                    pass
                    '''In this block you will put code the that will read the task from task.txt file and
                     print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
                     You can do it in this way:
                        - Read a line from the file
                        - Split the line where there is comma and space.
                        - Check if the username of the person logged in is the same as the username you have
                        read from the file.
                        - If they are the same print it in the format of Output 2 in the task PDF'''

                    with open("tasks.txt", "r") as task_database:
                        all_tasks = task_database.read()
                        # opening our task database

                    all_tasks = all_tasks.replace("\n", ", ")
                    tasks_formatted = all_tasks.split(", ")
                    # getting rid of interfering characters

                    structure_user = []  # 0, 6..
                    structure_taskname = []  # 1, 7 etc..
                    structure_task_description = []  # 2
                    structure_assigned_date = []  # 3
                    structure_due_date = []  # 4
                    structure_task_status = []  # 5
                    # appending taskline details

                    for i, value in enumerate(tasks_formatted):
                        if i % 6 == 0:
                            structure_user.append(value)
                        if i % 6 == 1:
                            structure_taskname.append(value)
                        if i % 6 == 2:
                            structure_task_description.append(value)
                        if i % 6 == 3:
                            structure_assigned_date.append(value)
                        if i % 6 == 4:
                            structure_due_date.append(value)
                        if i % 6 == 5:
                            structure_task_status.append(value)
                            # appending taskline details

                    counter = 0
                    for j in range(0, len(structure_user)):
                        # again, there should be as many iterations of the username as there are total task,
                        # because every individual task is assigned to a user, even if it's the same user over and over

                        if structure_user[j] == user_username.replace(",", ""):
                            # we need to identify the current user that's logged in, they want to view /their/ tasks
                            # if the username in the given task is equal to the username of the user that is currently
                            # logged in:
                            counter += 1
                            # count +1, then we can tell the current user how many tasks they have

                            taskline_vm = f"{structure_user[j]}, {structure_taskname[j]}, " \
                                          f"{structure_task_description[j]}, " \
                                          f"{structure_assigned_date[j]}, {structure_due_date[j]}, " \
                                          f"{structure_task_status[j]}"
                            # store the task line as usual, the only difference here is only the current user's tasks
                            # get iterated and stored, whilst other tasks from other users are not stored, just
                            # iterated

                            print(f"Task #:\t\t\t\t\t\t\t\t {counter}")
                            print(f"Assigned user:\t\t\t\t\t\t {structure_user[j]}\n"
                                  f"Task name:\t\t\t\t\t\t\t {structure_taskname[j]}\n"
                                  f"Task description:\t\t\t\t\t {structure_task_description[j]}\n"
                                  f"Date assigned:\t\t\t\t\t\t {structure_assigned_date[j]}\n"
                                  f"Date due:\t\t\t\t\t\t\t {structure_due_date[j]}\n"
                                  f"Task Complete:\t\t\t\t\t\t {structure_task_status[j]}\n")
                            # displaying details to the user

                            tasklines.append(taskline_vm)
                            # append current users into an empty list, made at the beginning of the application
                            # called tasklines, we use this to store the complete task database in a variable
                            # but also within context, e.g. we're currently only storing the current user's tasks
                            # in another menu we may append in all tasks, or all uncompleted tasks.. etc

                    if len(tasklines) == 1:
                        print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} task.\n")
                    elif len(tasklines) == 0:
                        print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} no tasks.\n")
                    else:
                        print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} total tasks.\n")
                    # depending on the total, we'll display this sentence differently

                elif user_choice == "ds":
                    pass
                    """1. Now format your program so that: a. Only the user with the username ‘admin’ is allowed to 
                    register users. b. The admin user is provided with a new menu option that allows them to display 
                    statistics. When this menu option is selected, the total number of tasks and the total number of 
                    users should be displayed in a user-friendly manner. """

                    with open("tasks.txt", "r") as task_database:
                        all_tasks = task_database.read()

                    all_tasks = all_tasks.replace("\n", ", ")
                    tasks_formatted = all_tasks.split(", ")
                    structure_user = []  # 0, 6..
                    structure_taskname = []  # 1, 7 etc..
                    structure_task_description = []  # 2
                    structure_assigned_date = []  # 3
                    structure_due_date = []  # 4
                    structure_task_status = []  # 5

                    for i, value in enumerate(tasks_formatted):
                        if i % 6 == 0:
                            structure_user.append(value)
                        if i % 6 == 1:
                            structure_taskname.append(value)
                        if i % 6 == 2:
                            structure_task_description.append(value)
                        if i % 6 == 3:
                            structure_assigned_date.append(value)
                        if i % 6 == 4:
                            structure_due_date.append(value)
                        if i % 6 == 5:
                            structure_task_status.append(value)

                    unique_user = []
                    # here we want a list that will report back a list of unique users, a unique user is a user whose
                    # account name may appear more than once, but appears at least once
                    tasks_complete = 0
                    # if the value of task status is set to yes, this will count upward, we will then report this back

                    for i in structure_user:
                        # for the username element
                        if i not in unique_user:
                            # if the username is not in our list, add it in, otherwise continue
                            unique_user.append(i)

                    for i in structure_task_status:
                        # for the 'task status' element
                        if structure_task_status == "Yes":
                            # if the value is "Yes" this means the task is complete
                            tasks_complete += 1
                            # then count

                    for i in range(0, len(unique_user)):
                        # we're using i in range + len, because we want i to be a number
                        # if 'i' is a number we can use its value to iterate through our lists
                        print(f"{unique_user[i]} has {structure_user.count(unique_user[i])} tasks.")
                        # prints "user" has "amount" tasks, whilst cycling through list of unique users
                        # this line of code is interesting, it checks the unique user list, because we only want to be
                        # told how many tasks a /user/ has just once!, however it checks the usernames list to count
                        # the tasks, and this is because if a user has e.g. 7 tasks, their name will appear 7 times

                    print(f"There are {len(unique_user)} total unique users.\n"
                          # len(unique_users) gives us the amount of users
                          f"There are {tasks_complete}/{len(structure_user)} tasks complete. "
                          f"({int((tasks_complete/len(structure_user)) * 100)}%)\n")
                    # prints the tasks complete/total tasks to give you an amount

                elif user_choice == "e":
                    print('Goodbye!!!')
                    exit()

                else:
                    print("You have made a wrong choice, Please Try again")

        elif user_password == user_database_list[username_index + 1]:
            print("Login successful!")

            break
        # TODO: USER MENU

    elif (user_username + ",") not in user_database_list:
        print(f"The username, '{user_username}' does not exist. Please contact administrator to create a new user or "
              f"try again.")
        # if the user enters a username that doesn't exist, they are prompted to either try again or contact admin.
        # contact admin would prompt for real life scenario where admin will create the user account

        while True:
            retry = input("Try again?\n"
                          "Yes:\t\t\t [Y]\n"
                          "No:\t\t\t\t [N]\n").lower()
            # a mistake that takes some getting used to is having the user input inside the while True code block,
            # this means we can allow the user to retry given they have an incorrect input

            # when we don't have an input prompt inside the while True block, the user is not given a chance to update
            # a given variable and forced/locked into an infinite loop

            if retry == "y":
                break
            elif retry == "n":
                print("Exiting application")
                exit()
            else:
                print("You have entered an incorrect value.\n")
                continue

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    user_choice = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if user_choice == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif user_choice == 'a':
        '''In this block you will put code that will allow a user to add a new task to task.txt file
                            - You can follow these steps:
                                - Prompt a user for the following: 
                                    - A username of the person whom the task is assigned to,
                                    - A title of a task,
                                    - A description of the task and 
                                    - the due date of the task.
                                - Then get the current date.
                                - Add the data to the file task.txt and
                                - You must remember to include the 'No' to indicate if the task is complete.'''

        while True:
            # we begin with while True, because if the user fails we want them to keep trying until
            # otherwise, or quit
            assigned_user = input("Which user is this task assigned to?\n")
            assigned_user = assigned_user + ","
            if assigned_user in user_database_list:
                assigned_user_index = user_database_list.index(assigned_user)
                # who is the task assigned to? if the value exists, we can proceed, however furthermore
                # because we're using a list, what if the "username" is actually someone's password? the
                # pass would exist, but it is not a username. we know that passwords are only at odd
                # indexes, so let's ensure that the "username" is not located at an odd index
                if assigned_user in user_database_list and assigned_user_index % 2 == 0:
                    pass
                    # if the assigned user is in the database, and at an even index, continue

            elif assigned_user not in user_database_list:
                print("The user does not exist, please create user or try again.")
                # if the value is not in the list, prompt user to retry
                retry = input("Try again?\n"
                              "Yes:\t\t\t [Y]\n"
                              "No:\t\t\t\t [N]\n"
                              "Quit:\t\t\t [Q]\n").lower()
                if retry == "y":
                    continue
                    # allows user to attempt again
                elif retry == "n":
                    break
                    # allows user to return to menu
                elif retry == "q":
                    print("Exiting application")
                    exit()
                    # allows user to exit application
                else:
                    print("You have entered an incorrect value.\n")
                    # loops user as they have entered bad input

            task_title = input("What is the title of the task?\n")
            task_title = task_title.replace(",", "")
            # the name of the task is stored in a variable, note that we re-save their input - because
            # the nature of our database, commas interrupt our application's interpretation of the database
            # we will repeat this for each applicable value

            task_description = input("What is the task description?\n")
            task_description = task_description.replace(",", "")
            # user describes the task

            task_due_day = int(input("Task Due (Day):\n"))
            task_due_month = int(input("Task Due (Month):\n"))
            task_due_year = int(input("Task Due (Year):\n"))
            # user enters integer values that make up the date

            task_due_date = datetime.date(task_due_year, task_due_month, task_due_day)
            task_due_date = task_due_date.strftime("%d,%b,%Y")
            # we have imported a date/time module that allows us to fuse mathematical logic and apply it
            # with the structure of dates, we have our integer values that represent a respective date,
            # the date module converts this into a date object
            # in addition, we then convert this into a string that can be written to task database, in the
            # same format as the example dates that already exist
            # the strftime("%d,%b,%Y") values are conversion values,
            # %d = numbered day, 1-31
            # %b = short formed month, Jan-Dec
            # %Y = full form century, 0-9999

            # TODO: note, retrospectively I am of the fact that I can convert these values with out the
            #  the commas, however at the time of coding I was under the impression that I had to further
            #  manipulate the converted string to thus remove the commas

            task_due_date = task_due_date.replace(",", " ")
            # the converted string produces commas, so we manipulate the string to remove them
            current_time = datetime.datetime.today()
            # probably my favourite feature of the datetime module, the ability to work with the micro
            # second that you run the program, the task assigned feature is set to the current time the user
            # sets the task

            task_assigned_date = current_time.strftime("%d,%b,%Y")
            # we need the assigned date in the same format we have the due date,
            task_assigned_date = task_assigned_date.replace(",", " ")
            # we manipulate the converted date string

            task_status = "No"
            # all tasks have a status, as the task is set this status is set automatically to No, as the
            # task won't be complete when it's just being set. in later menu option we will have a chance
            # to change the status

            taskline = (f"\n{assigned_user} {task_title}, {task_description}, "
                        f"{task_assigned_date}, {task_due_date}, {task_status}")

            # the line that the user has created through their inputs is formed and stored in a variable
            # note that it begins with \n, we want to ensure that this is on a new line
            # note that assigned user has no comma following its value - this is because we actually work
            # with the username's value and the comma, the comma is in a way already there
            # the alternative to this would be reverting the value back to the value without the comma, or
            # storing the two values into two different variables

            with open("tasks.txt", "a+") as task_database:
                task_database.write(taskline)
                # we write this to our task database
                # this is in append mode, so the task will be added to the end of the file

        with open("tasks.txt", "r") as task_database:
            all_tasks = task_database.read()
            # opening the file to read its contents into a variable

        all_tasks = all_tasks.replace("\n", ", ")
        # when we read the file, there are escape characters, these escape characters are understood as to
        # us as spaces, but by the computer as "\n", ultimately we need to treat this as ", " because
        # that's how we want to segment our sentences that form 1 given task

        # e.g.
        # task_user, task_name, task_descript\n
        # task_user2, task_name2, task_descript2\n becomes
        # task_user, task_name, task_descrip, task_user2, task_name2, task_descript,

        tasks_formatted = all_tasks.split(", ")
        # splitting by the ", " *comma space
        # these are the values we need, these values are sequential. so we know that every 0th/6th value is
        # going to be the user's name, every 1st and 7th value is going to be a task name

        structure_user = []  # 0, 6..
        structure_taskname = []  # 1, 7 etc..
        structure_task_description = []  # 2
        structure_assigned_date = []  # 3
        structure_due_date = []  # 4
        structure_task_status = []  # 5

        for i, value in enumerate(tasks_formatted):
            if i % 6 == 0:
                structure_user.append(value)
            if i % 6 == 1:
                structure_taskname.append(value)
            if i % 6 == 2:
                structure_task_description.append(value)
            if i % 6 == 3:
                structure_assigned_date.append(value)
            if i % 6 == 4:
                structure_due_date.append(value)
            if i % 6 == 5:
                structure_task_status.append(value)

            # enumerate allows us to work with the index and the index value
            # if we modulo the index by the total number of detail in sequence, the outcome/remainder is the
            # index of the value

            # in other words, the first value is a username, the username is at index 0
            # in a taskline, there are 6 details, if we modulo 0 by 6 we will get 0, this is the username
            # if we modulo 1 by 6, we'll get 1, and if we increment e.g. 2 by 6 will get 2

        counter = 0
        # counter is used to give a task a corresponding task number
        for i in range(0, len(structure_user)):
            # it is okay to use structure_user to iterate, as there should be as much "users" as there are
            # tasks lines
            counter += 1
            # task 1 should start at 1, humans don't count like computers
            print(f"Task #:\t\t\t\t\t\t\t\t {counter}")
            print(f"Assigned user:\t\t\t\t\t\t {structure_user[i]}\n"
                  f"Task name:\t\t\t\t\t\t\t {structure_taskname[i]}\n"
                  f"Task description:\t\t\t\t\t {structure_task_description[i]}\n"
                  f"Date assigned:\t\t\t\t\t\t {structure_assigned_date[i]}\n"
                  f"Date due:\t\t\t\t\t\t\t {structure_due_date[i]}\n"
                  f"Task Complete:\t\t\t\t\t\t {structure_task_status[i]}\n")

    elif user_choice == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

        with open("tasks.txt", "r") as task_database:
            all_tasks = task_database.read()
            # opening the file to read its contents into a variable

        all_tasks = all_tasks.replace("\n", ", ")
        # when we read the file, there are escape characters, these escape characters are understood as to
        # us as spaces, but by the computer as "\n", ultimately we need to treat this as ", " because
        # that's how we want to segment our sentences that form 1 given task

        # e.g.
        # task_user, task_name, task_descript\n
        # task_user2, task_name2, task_descript2\n becomes
        # task_user, task_name, task_descrip, task_user2, task_name2, task_descript,

        tasks_formatted = all_tasks.split(", ")
        # splitting by the ", " *comma space
        # these are the values we need, these values are sequential. so we know that every 0th/6th value is
        # going to be the user's name, every 1st and 7th value is going to be a task name

        structure_user = []  # 0, 6..
        structure_taskname = []  # 1, 7 etc..
        structure_task_description = []  # 2
        structure_assigned_date = []  # 3
        structure_due_date = []  # 4
        structure_task_status = []  # 5

        for i, value in enumerate(tasks_formatted):
            if i % 6 == 0:
                structure_user.append(value)
            if i % 6 == 1:
                structure_taskname.append(value)
            if i % 6 == 2:
                structure_task_description.append(value)
            if i % 6 == 3:
                structure_assigned_date.append(value)
            if i % 6 == 4:
                structure_due_date.append(value)
            if i % 6 == 5:
                structure_task_status.append(value)

            # enumerate allows us to work with the index and the index value
            # if we modulo the index by the total number of detail in sequence, the outcome/remainder is the
            # index of the value

            # in other words, the first value is a username, the username is at index 0
            # in a taskline, there are 6 details, if we modulo 0 by 6 we will get 0, this is the username
            # if we modulo 1 by 6, we'll get 1, and if we increment e.g. 2 by 6 will get 2

        counter = 0
        # counter is used to give a task a corresponding task number
        for i in range(0, len(structure_user)):
            # it is okay to use structure_user to iterate, as there should be as much "users" as there are
            # tasks lines
            counter += 1
            # task 1 should start at 1, humans don't count like computers
            print(f"Task #:\t\t\t\t\t\t\t\t {counter}")
            print(f"Assigned user:\t\t\t\t\t\t {structure_user[i]}\n"
                  f"Task name:\t\t\t\t\t\t\t {structure_taskname[i]}\n"
                  f"Task description:\t\t\t\t\t {structure_task_description[i]}\n"
                  f"Date assigned:\t\t\t\t\t\t {structure_assigned_date[i]}\n"
                  f"Date due:\t\t\t\t\t\t\t {structure_due_date[i]}\n"
                  f"Task Complete:\t\t\t\t\t\t {structure_task_status[i]}\n")

    elif user_choice == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

        with open("tasks.txt", "r") as task_database:
            all_tasks = task_database.read()
            # opening our task database

        all_tasks = all_tasks.replace("\n", ", ")
        tasks_formatted = all_tasks.split(", ")
        # getting rid of interfering characters

        structure_user = []  # 0, 6..
        structure_taskname = []  # 1, 7 etc..
        structure_task_description = []  # 2
        structure_assigned_date = []  # 3
        structure_due_date = []  # 4
        structure_task_status = []  # 5
        # appending taskline details

        for i, value in enumerate(tasks_formatted):
            if i % 6 == 0:
                structure_user.append(value)
            if i % 6 == 1:
                structure_taskname.append(value)
            if i % 6 == 2:
                structure_task_description.append(value)
            if i % 6 == 3:
                structure_assigned_date.append(value)
            if i % 6 == 4:
                structure_due_date.append(value)
            if i % 6 == 5:
                structure_task_status.append(value)
                # appending taskline details

        counter = 0
        for j in range(0, len(structure_user)):
            # again, there should be as many iterations of the username as there are total task,
            # because every individual task is assigned to a user, even if it's the same user over and over

            if structure_user[j] == user_username.replace(",", ""):
                # we need to identify the current user that's logged in, they want to view /their/ tasks
                # if the username in the given task is equal to the username of the user that is currently
                # logged in:
                counter += 1
                # count +1, then we can tell the current user how many tasks they have

                taskline_vm = f"{structure_user[j]}, {structure_taskname[j]}, " \
                              f"{structure_task_description[j]}, " \
                              f"{structure_assigned_date[j]}, {structure_due_date[j]}, " \
                              f"{structure_task_status[j]}"
                # store the task line as usual, the only difference here is only the current user's tasks
                # get iterated and stored, whilst other tasks from other users are not stored, just
                # iterated

                print(f"Task #:\t\t\t\t\t\t\t\t {counter}")
                print(f"Assigned user:\t\t\t\t\t\t {structure_user[j]}\n"
                      f"Task name:\t\t\t\t\t\t\t {structure_taskname[j]}\n"
                      f"Task description:\t\t\t\t\t {structure_task_description[j]}\n"
                      f"Date assigned:\t\t\t\t\t\t {structure_assigned_date[j]}\n"
                      f"Date due:\t\t\t\t\t\t\t {structure_due_date[j]}\n"
                      f"Task Complete:\t\t\t\t\t\t {structure_task_status[j]}\n")
                # displaying details to the user

                tasklines.append(taskline_vm)
                # append current users into an empty list, made at the beginning of the application
                # called tasklines, we use this to store the complete task database in a variable
                # but also within context, e.g. we're currently only storing the current user's tasks
                # in another menu we may append in all tasks, or all uncompleted tasks.. etc

        if len(tasklines) == 1:
            print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} task.\n")
        elif len(tasklines) == 0:
            print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} no tasks.\n")
        else:
            print(f"{user_username}:\t\t\t\t\t\t\t\t {len(tasklines)} total tasks.\n")
        # depending on the total, we'll display this sentence differently

    elif user_choice == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
