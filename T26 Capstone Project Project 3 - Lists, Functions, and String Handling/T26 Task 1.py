# =====importing libraries===========
'''This is the section where you will import libraries'''
import datetime

"""
IMRPOVEMENTS:
* now does not mirrors usernames that are not identical because they differ in case sensitivity
e.g. you cannot register "ADMIN" if you have "admin" 
* code now comes with functions with descriptions to produce bite size version of Capstone 2
* due date is now checked and cannot be a past date
* additional options for generating report style
"""


def read_user_database(user_filename, read_plus):
    """
    :param user_filename: contains usernames and passwords on each line separated by comma space
    :param read_plus: "r+" ideally
    :return: returns the usernames and passwords in a dictionary
    """
    # we made a function to read the user database
    # takes two arguments, the file containing the usernames and read mode
    with open(user_filename, read_plus) as f:
        username_file = f.readlines()
        # we want each line as an element = ['admin, adm1n\n', 'lekky, lol']

    sort_usernames = []
    # we need to clean the usernames of characters such as "\n" and append into sort_usernames
    for i in username_file:
        if "\n" in i:
            i = i.replace("\n", "")
            # if "\n" is in the element lets remove it by replacing it with nothing
        sort_usernames.append(i)
        # append our values into our list

    username_tuples = []
    # we will use this list to create tuples, then we'll dictionary the tuples
    for i in sort_usernames:
        i = i.split(", ")
        # we split the elements by the comma space
        i = (i[0], i[1])
        # and reassign i to become a tuple of the split elements
        username_tuples.append(i)
        # we'll append the tuples into our tuples list
    create_dictionary = dict(username_tuples)
    # then create a dictionary
    return create_dictionary
    # return the dictionary value back to me


def read_task_database(task_filename, read_plus):  # this is going to store tasks into workable variables
    with open(task_filename, read_plus) as f:
        tasks_files = f.readlines()

    user = []
    task_name = []
    task_description = []
    date_assigned = []
    date_due = []
    task_status = []
    counter = 0
    #  these are empty lists used to append in the respective elements

    for line in tasks_files:
        line = line.split(",")
        # for each task, we split the task into each element, the seperate details of the task
        for info in line:
            if "\n" in info:
                info = info.replace("\n", "")
            # we check for new line characters that will interfer with our set up and remove them
            if counter % 6 == 0:
                user.append(info)
            elif counter % 6 == 1:
                task_name.append(info)
            elif counter % 6 == 2:
                task_description.append(info)
            elif counter % 6 == 3:
                date_assigned.append(info)
            elif counter % 6 == 4:
                date_due.append(info)
            elif counter % 6 == 5:
                task_status.append(info)
            # we append these elements into their respective list for later use

            counter += 1


def admin_reg_user():  # should not duplicate names
    print("Register new user")

    while True:
        case_sensitivity = []  # this is going to check that the user doesn't add a username that exists already
        # but with a different arrangement case-sensitive letters, it will convert all values (users new username)
        # and the values in our database into uppercase/capitals and see if any are identical
        for i in username_profiles:  # TODO: test with replace "user_database
            i = i.upper()
            case_sensitivity.append(i)

        new_username = input("What is the new username?\n"
                             ":")
        if new_username in user_database:
            print("The user already exists, please try again.")
            attempt_username = continue_prompt()
            continue_quit(attempt_username)

        elif new_username.upper() in case_sensitivity:
            print("Your username mirrors another user with differing case sensitivity, please try again")
            attempt_username = continue_prompt()
            continue_quit(attempt_username)

        elif new_username not in user_database:
            confirm_username = input("Please confirm the new username\n"
                                     ":")
            if confirm_username == new_username:
                print("Username confirmed")
                break
            elif confirm_username != new_username:
                print("The usernames do not match, please try again.")
                attempt_username = continue_prompt()
                continue_quit(attempt_username)

    while True:
        new_username_pass = input("What is the new username password?\n"
                                  ":")
        confirm_password = input("Please confirm the new username password\n"
                                 ":")
        if confirm_password == new_username_pass:
            print("Password confirmed")
            break
        elif confirm_password != new_username_pass:
            print("The passwords do not match, please try again.")
            attempt_username = continue_prompt()
            continue_quit(attempt_username)

    with open("user.txt", "a+") as f:
        f.write(f"\n{new_username}, {new_username_pass}")

    print("Username has been created!")
    display_names = read_user_database("user.txt", "r+")
    for i in display_names.keys():
        print(i)
    print("")
    print_menu()


def add_task(task_filename, read_plus):
    while True:
        which_user = input("Who is the task assigned to?\n"
                           ":")
        if which_user not in username_profiles:
            print("The user does not exist, please contact admin to create user or try again")
            add_task_attempt = continue_prompt()
            continue_quit(add_task_attempt)
            # if the username being assigned a task is not in the database, the user entered the wrong name or
            # needs to create that user

        elif which_user in username_profiles:
            assigned_user = which_user
            # if they exist, we store the detail for later use
            break

    task_title = input("What is the name of the task?\n"
                       ":")
    task_title = task_title.replace(",", "")
    # store task title element and also remove commas that will interfere with the program
    task_description = input("What does the task entail?\n"
                             ":")
    task_description = task_description.replace(",", "-")
    # store task description, and remove commas that will interfere
    while True:
        current_time = datetime.datetime.today()
        # this variable uses the datetime module and stores the current moment

        task_due_day = int(input("Task Due (Day):\n"
                                 ":"))
        # user sets the due date: day
        task_due_month = int(input("Task Due (Month):\n"
                                   ":"))
        # user sets the due date: month

        task_due_year = int(input("Task Due (Year):\n"
                                  ":"))
        # user sets the due date: year

        task_due_date = datetime.datetime(task_due_year, task_due_month, task_due_day)
        check_task_due_date = task_due_date
        # the task due date is composed of the elements set by the user, they are passed in as arguments
        # task due date is saved into another variable, so we can create a string out of task due date but keep
        # its datetime object properties in check task due date
        verify_date = datetime.datetime.now()  # (task_due_year, task_due_month, task_due_day, 0, 0, 0)

        task_due_date = task_due_date.strftime("%d %b %Y")
        # we convert the due date into the same date format as the task database
        # (Number/Day, Abbreviate/Month, Number/Year)

        time_deduction = datetime.timedelta(0)
        a_day_ahead = current_time + datetime.timedelta(0.25)
        # a day a head is the current time, +1/4 day
        a_moment_ago = current_time - time_deduction

        # we use datetime.timedelta() to manipulate time like maths, 1 is equal to 24 hours, so e.g. 0.5 would be 12
        # time_deduction = 0 (or, now) if the task is set before now (or now), then that is qutie unfair
        # a_day_ahead = anything within 24 hours (for argument's sake) is set too soon

        if check_task_due_date < a_moment_ago:  # you can't set a task due for date earlier than now
            print(f"The task due date: \"{check_task_due_date}\", \"{verify_date.strftime('%d %b %Y')}\"\n"
                  f"is set before the current time: \"{a_moment_ago}\", \"{a_moment_ago.strftime('%d %b %Y')}\"\n"
                  f"Due date cannot be a past time or current time")
            attempt_set_task = continue_prompt()
            continue_quit(attempt_set_task)
            # if the task is set too soon, give the user a chance to redo or quit

        elif check_task_due_date < a_day_ahead:  # you can't set a task due within 6 hours
            print(f"The task due date: \"{check_task_due_date}\", \"{verify_date.strftime('%d %b %Y')}\"\n"
                  f"is set too soon: \"{a_day_ahead}\", \"{a_day_ahead.strftime('%d %b %Y')}\"\n"
                  f"Please allow at least more than a quarter a day to set due date.")
            attempt_set_task = continue_prompt()
            continue_quit(attempt_set_task)
            # if the task is set with not enough time, give the user a chance to redo or quit

        elif verify_date > a_moment_ago and a_day_ahead:
            # if the due date is greater than a moment ago (redundant i know), and a day ahead, continue
            break

    task_assigned_date = current_time.strftime("%d %b %Y")
    task_status = input("Is the task complete?\n"
                        "Yes\t\t\t\t\t\t Y\n"
                        "No\t\t\t\t\t\t N\n").upper()
    if task_status == "Y":
        task_status = "Yes"
    elif task_status == "N":
        task_status = "No"
    else:
        print("You've entered an incorrect value.")
        task_status_attempt = continue_prompt()
        continue_quit(task_status_attempt)

    taskline = (f"\n{assigned_user}, {task_title}, {task_description}, "
                f"{task_assigned_date}, {task_due_date}, {task_status}")

    with open(task_filename, read_plus) as task_database:
        task_database.write(f"{taskline}")
    print(f"Task has been written to {task_database}")
    print_menu()


def view_all(task_filename, read_plus):
    """

    :param task_filename: takes the file with tasks set to each line, separated by 5 commas
    :param read_plus: set to r+
    :return: does not return a value, this function will count each task line and organise it into presentable data
    """
    with open(task_filename, read_plus) as f:
        tasks_files = f.readlines()

    user = []
    task_name = []
    task_description = []
    date_assigned = []
    date_due = []
    task_status = []
    counter = 0

    for line in tasks_files:
        line = line.split(",")
        for info in line:
            if "\n" in info:
                info = info.replace("\n", "")
            if counter % 6 == 0:
                user.append(info)
            elif counter % 6 == 1:
                task_name.append(info)
            elif counter % 6 == 2:
                task_description.append(info)
            elif counter % 6 == 3:
                date_assigned.append(info)
            elif counter % 6 == 4:
                date_due.append(info)
            elif counter % 6 == 5:
                task_status.append(info)

            counter += 1

    task_menu = []
    counter = 0
    for i in user:
        details = (f"Task #:\t\t\t\t\t\t\t\t  {counter}\n"
                   f"User:\t\t\t\t\t\t\t\t  {user[counter]}\n"
                   f"Task name:\t\t\t\t\t\t\t {task_name[counter]}\n"
                   f"Task description\t\t\t\t\t {task_description[counter]}\n"
                   f"Date assigned:\t\t\t\t\t\t {date_assigned[counter]}\n"
                   f"Date due:\t\t\t\t\t\t\t {date_due[counter]}\n"
                   f"Task status:\t\t\t\t\t\t {task_status[counter]}\n")

        task_tuples = (counter, details)
        counter += 1
        task_menu.append(task_tuples)

    task_dictionary = dict(task_menu)
    for i in task_dictionary.values():
        print(i)


def view_mine(task_filename, read_plus):
    pass
    """Add functionality to view specific tasks
    mark as complete or incomplete 
    edit tasks
    -1 to return to main menu"""
    """

    :param task_filename: takes the file with tasks set to each line, separated by 5 commas
    :param read_plus: set to r+
    :return: does not return a value, this function will count each task line and organise it into presentable data
    """
    with open(task_filename, read_plus) as f:
        tasks_files = f.readlines()

    user = []
    task_name = []
    task_description = []
    date_assigned = []
    date_due = []
    task_status = []
    counter = 0

    for line in tasks_files:
        line = line.split(",")
        for info in line:
            if "\n" in info:
                info = info.replace("\n", "")
            if counter % 6 == 0:
                user.append(info)
            elif counter % 6 == 1:
                task_name.append(info)
            elif counter % 6 == 2:
                task_description.append(info)
            elif counter % 6 == 3:
                date_assigned.append(info)
            elif counter % 6 == 4:
                date_due.append(info)
            elif counter % 6 == 5:
                task_status.append(info)

            counter += 1

    task_menu = []
    counter = 0
    personal_tasks_counter = 1
    for i in user:
        if i == user_login:

            details = (f"Task #:\t\t\t\t\t\t\t\t  {personal_tasks_counter}\n"
                       f"User:\t\t\t\t\t\t\t\t  {user[counter]}\n"
                       f"Task name:\t\t\t\t\t\t\t {task_name[counter]}\n"
                       f"Task description\t\t\t\t\t {task_description[counter]}\n"
                       f"Date assigned:\t\t\t\t\t\t {date_assigned[counter]}\n"
                       f"Date due:\t\t\t\t\t\t\t {date_due[counter]}\n"
                       f"Task status:\t\t\t\t\t\t {task_status[counter]}\n")

            task_tuples = (personal_tasks_counter, details)
            task_menu.append(task_tuples)
            counter += 1
            personal_tasks_counter += 1

            print(details)
        elif i != user_login:
            counter += 1
            continue

    task_dictionary = dict(task_menu)

    # we now have a menu for our current users task, now we want to let the user manipulate that menu

    while True:
        try:

            selected_task_to_edit = int(input("Would you like to edit a task?\n"
                                              "Enter task number or input -1 to exit\n"
                                              ":"))

            if isinstance(selected_task_to_edit, int) and len(task_dictionary) >= selected_task_to_edit != -1:
                print(task_dictionary[selected_task_to_edit])
                edit_this_task = input("Would you like to edit this task?\n"
                                       "Yes:\t\t\t\t\t\t Y\n"
                                       "No:\t\t\t\t\t\t\t N\n"
                                       ":").upper()
                if edit_this_task == "Y":  # TODO: ARGHHH TEDIT THIS
                    task_description_redo = str(input("What does the task entail?\n"
                                                      ":"))
                    task_description_redo = task_description_redo.replace(",", "-")

                    edited_task = f"{user[selected_task_to_edit]},{task_name[selected_task_to_edit]}, {task_description_redo},{date_assigned[selected_task_to_edit]},{date_due[selected_task_to_edit]},{task_status[selected_task_to_edit]} "

                    find_task = f"{user[selected_task_to_edit]},{task_name[selected_task_to_edit]},{task_description[selected_task_to_edit]},{date_assigned[selected_task_to_edit]},{date_due[selected_task_to_edit]},{task_status[selected_task_to_edit]}\n"

                    with open("tasks.txt", "r+") as editing_f:
                        tasks_contents = editing_f.read()

                    tasks_contents = tasks_contents.replace(find_task, edited_task + "\n")

                    with open("tasks.txt", "w") as overwriting_f:
                        overwriting_f.write(tasks_contents)

                    print("Task in file has been re-written.")
                    break



            elif isinstance(selected_task_to_edit, str):
                print("You have not entered a respective task number!.")

            elif selected_task_to_edit == -1:
                minus_one = continue_prompt()
                continue_quit(minus_one)

            elif isinstance(selected_task_to_edit, int) and len(task_dictionary) < selected_task_to_edit:
                print("You do not have that many tasks!")
                you_dont_have_that_much_to_do = continue_prompt()
                continue_quit(you_dont_have_that_much_to_do)

            else:
                print("How did you get here?")

        except ValueError as wrongness:
            print(wrongness)
            print("You have not entered a respective task number.\n")
            that_not_an_int = continue_prompt()
            continue_quit(that_not_an_int)


def generate_task_report(task_filename, read_plus):
    with open(task_filename, read_plus) as f:
        tasks_files = f.readlines()
        # opening the file as listed lines because we want to work with each line

    listed_tasks = []
    # once we sort our tasks on each line, we'll append them into this list

    for line in tasks_files:
        line = line.split(", ")
        listed_tasks.append(line)
        # split by comma space and append the elements into our list
    # listed_tasks is now a nested list, a list containing several lists that composes

    task_tuples = []

    for i in enumerate(listed_tasks):
        task_tuples.append(i)
        # in this loop, when we iterate through our list of lists, it will assign a number to each list,
        # by doing this we'll be establishing a pattern and we will be able to cast this pattern to a dictionary
        # the dictionary will consist of numbers as keys, and lists as values

    task_statistics_database = dict(task_tuples)

    count_tasks = 0
    count_complete_tasks = 0
    count_incomplete_tasks = 0
    count_incomplete_overdue_tasks = 0
    # when we iterate through our dictionary we will check for these values and +=1 if applicable

    for i in task_statistics_database.values():
        count_tasks += 1
        if i[5] == "No" or i[5] == "No\n":
            count_incomplete_tasks += 1
        if i[5] == "Yes" or i[5] == "Yes\n":
            count_complete_tasks += 1
        # 1) count tasks, this can be done on each iteration
        # 2) count tasks status being incomplete, done by i5, the 5th element is set to No
        # 3) alternatively count task complete if it is set to Yes

        convert_due_date = datetime.datetime.strptime(i[4], "%d %b %Y")
        current_time = datetime.datetime.today()
        # we convert the string value at i[4] (due date) into an object
        # we establish a current time, time object

        if current_time > convert_due_date:
            count_incomplete_overdue_tasks += 1
        # 4) if now surpasses the due date, than we are currently overdue on this task,

    percentage_incomplete = (count_incomplete_tasks / count_tasks) * 100
    percentage_incomplete_overdue = (count_incomplete_overdue_tasks / count_tasks) * 100
    # these values will calculate the percentage of incomplete and incomplete/overdue tasks compared to the total
    # amount tasks

    report = f"Task report\n" \
             f"Total number of tasks:\t\t\t\t\t\t\t\t\t\t\t{count_tasks}\n" \
             f"Total number of completed tasks:\t\t\t\t\t\t\t\t{count_complete_tasks}\n" \
             f"Total number of incomplete tasks:\t\t\t\t\t\t\t\t{count_incomplete_tasks}\n" \
             f"Total number of incomplete & overdue tasks:\t\t\t\t\t\t{count_incomplete_overdue_tasks}\n" \
             f"Percent of incomplete tasks:\t\t\t\t\t\t\t\t\t{percentage_incomplete}%\n" \
             f"Percent of incomplete & overdue tasks:\t\t\t\t\t\t\t{percentage_incomplete_overdue}%\n"

    print(report)
    # the report takes these details and writes a valuable string

    with open("tasks_report.txt", "w") as generate_report:
        generate_report.write(report)
        # it generates a text report

    print(f"Report for \"{task_filename}\" has been written and saved to {generate_report}")
    # and lets user know
    print_menu()


def generate_user_report(task_filename, read_plus):
    current_time = datetime.datetime.today()
    with open(task_filename, read_plus) as f:
        tasks_files = f.readlines()

    listed_tasks = []

    for line in tasks_files:
        line = line.split(", ")
        listed_tasks.append(line)

    task_tuples = []

    for i in enumerate(listed_tasks):
        task_tuples.append(i)
    user_statistics_database = dict(task_tuples)

    users = []
    for i in user_statistics_database.values():
        if i[0] not in users:
            users.append(i[0])

    count_users = []
    count_users_percentage = []
    count_user_completeness = []
    count_user_incompleteness = []
    count_user_incomplete_overdue = []

    for i in users:
        coupler = [i, 0]
        coupling = tuple(coupler)
        count_users.append(coupling)
        count_users_percentage.append(coupling)
        count_user_completeness.append(coupling)
        count_user_incompleteness.append(coupling)
        count_user_incomplete_overdue.append(coupling)

    user_task_count = dict(count_users)
    user_task_percentage = dict(count_users_percentage)
    user_task_completed = dict(count_user_completeness)
    user_task_incomplete = dict(count_user_incompleteness)
    user_task_incomplete_overdue = dict(count_user_incomplete_overdue)

    for i in user_statistics_database.values():
        # print(i[5]) # status condition
        # print(i) # list
        # print(i[0]) # name value
        if i[0] in user_task_count.keys():  # the username is in the list at index 0, i[0] goes to that user element
            user_task_count[i[0]] += 1
        if i[5] == "Yes" or i[5] == "Yes\n":
            user_task_completed[i[0]] += 1  # check i0
        elif i[5] == "No" or i[5] == "No\n":
            user_task_incomplete[i[0]] += 1
        convert_due_date = datetime.datetime.strptime(i[4], "%d %b %Y")
        if current_time > convert_due_date and (i[5] == "No" or i[5] == "No\n"):
            user_task_incomplete_overdue[i[0]] += 1

    tasks_sum = 0
    for i in user_task_count.values():
        tasks_sum += i

    for i in user_task_percentage:
        user_task_percentage[i] = (user_task_count[i] / tasks_sum) * 100

    for i in user_task_completed:
        user_task_completed[i] = (user_task_completed[i] / user_task_count[i]) * 100

    for i in user_task_incomplete:
        user_task_incomplete[i] = (user_task_incomplete[i] / user_task_count[i]) * 100

    for i in user_task_incomplete_overdue:
        user_task_incomplete_overdue[i] = (user_task_incomplete_overdue[i] / user_task_count[i]) * 100

    reporting_style = input("Select reporting style:\n"
                            "U\t\t\t\t\t\t\t by user.\n"
                            "D\t\t\t\t\t\t\t by task detail.\n").upper()

    if reporting_style == "U":
        with open("users_report.txt", "w") as generate_report:
            for i in users:
                generate_report.write((f"{i} has {user_task_count[i]} tasks\n"
                                       f"{i} has {user_task_percentage[i]}% of {tasks_sum} total tasks\n"
                                       f"{i} has {user_task_completed[i]}% of their tasks complete\n"
                                       f"{i} has {user_task_incomplete[i]}% of their tasks incomplete\n"
                                       f"{i} has {user_task_incomplete_overdue[i]}% of their tasks incomplete and "
                                       f"overdue\n"))

    elif reporting_style == "D":
        report = ""
        for i in users:
            reporting = f"{i} has {user_task_count[i]} tasks\n"
            report += reporting

        for i in users:
            reporting = f"{i} has {user_task_percentage[i]}% of {tasks_sum} total tasks\n"
            report += reporting

        for i in users:
            reporting = f"{i} has {user_task_completed[i]}% of their tasks complete\n"
            report += reporting

        for i in users:
            reporting = f"{i} has {user_task_incomplete[i]}% of their tasks incomplete\n"
            report += reporting

        for i in users:
            reporting = f"{i} has {user_task_incomplete_overdue[i]}% of their tasks incomplete and overdue\n"
            report += reporting

        with open("users_report.txt", "w") as generate_report:
            generate_report.write(report)

    print_menu()


def continue_prompt():
    """
    continue_prompt works after user has failed to input a respective key to a menu screen just prior
    this function will prompt to the user to either try again or quit application
    must be entered after print("incorrect value") and while True:
    pair with
    :return: returns the value for the user input for continue_quit
    """
    while True:
        user_input = input("Would you like to continue or quit?\n"
                           "Continue\t\t\t\t\t\t C\n"
                           "Quit\t\t\t\t\t\t\t Q\n"
                           ":").upper()
        if user_input == "C":
            break
        elif user_input == "Q":
            break
        else:
            pass

    return user_input


def continue_quit(continue_prompt_variable):
    """
    used for continue_prompt, store continue prompt into variable and pass variable into continue_quit
    :param continue_prompt_variable: stores the user choice from previous function
    :return:
    """

    if continue_prompt_variable == "C":
        pass
    elif continue_prompt_variable == "Q":
        print("Exiting application.")
        exit()


def print_menu():
    """
    simply prints our menu in an aesthetically pleasing way
    :return: n/a
    """
    print("Use respective keys to select from the menu:\n"
          "Register new user\t\t\t\t\t\t R\n"
          "Add new task\t\t\t\t\t\t\t A\n"
          "View all tasks\t\t\t\t\t\t\t VA\n"
          "View my tasks\t\t\t\t\t\t\t VM\n"
          "Generate task report\t\t\t\t\t GTR\n"
          "Generate user report\t\t\t\t\t GUR\n"
          "Exit application\t\t\t\t\t\t E\n")


user_database = read_user_database("user.txt", "r+")
username_profiles = user_database.keys()

# LOGIN
while True:
    user_login = input(
        "Please enter your username\n"  # login screen, having the ":" on next line is visually pleasing (UX/UI)
        ":")
    if user_login not in user_database:  # if the username isn't in the database, it doesn't exist, contact admin
        print("The username does not exist.\nPlease contact Admin to create user or try again.")
        users_choice = continue_prompt()  # our two functions back to back, cp() takes a choice from user
        continue_quit(users_choice)  # cq() takes the user choice and either continues or quits

    elif user_login in user_database and user_login != "admin":  # STANDARD USER LOGIN
        print(f"Hello {user_login}")

        while True:
            user_password = input("Please enter your password\n"
                                  ":")
            if user_password == user_database[user_login]:
                print("Login successful.")
                break  # TODO: either break or insert menu here, break leads to admin menu
                # TODO: we could have some options unlock for if the user is an admin by checking who has logged in

            elif user_password != user_database[user_login]:
                print("Password incorrect, please try again")
                attempt_password = continue_prompt()
                continue_quit(attempt_password)

        if user_password == user_database[user_login]:  # this is needed because when the user enters wrong password
            # then enters the correct password, they will be looped back to entering their username
            # this if statement catches and hold the relevant values, and breaks out of the outer loop to progress code
            break

    elif user_login in user_database and user_login == "admin":  # ADMIN USER LOGIN
        print(f"Administrative login")

        while True:
            user_password = input("Please enter your password\n"
                                  ":")
            if user_password == user_database[user_login]:
                print("Administrative login successful.")
                break

            elif user_password != user_database[user_login]:
                print("Password incorrect, please try again")
                attempt_password = continue_prompt()
                continue_quit(attempt_password)

        if user_password == user_database[user_login]:  # mirrors #TODO: LINE 189
            break

print("Welcome to Task Manager application\n"
      "\nUse respective keys to select from the menu:\n"
      "Register new user\t\t\t\t\t\t R\n"
      "Add new task\t\t\t\t\t\t\t A\n"
      "View all tasks\t\t\t\t\t\t\t VA\n"
      "View my tasks\t\t\t\t\t\t\t VM\n"
      "Generate task report\t\t\t\t\t GTR\n"
      "Generate user report\t\t\t\t\t GUR\n"
      "Exit application\t\t\t\t\t\t E\n")
# the menu is outside the loop, so it doesn't print obnoxiously

while True:
    user_choice = input(":").upper()

    if user_choice == "R" and user_login == "admin":
        admin_reg_user()

    elif user_choice == "R" and user_login != "admin":
        print("Administrator permission required")
        admin_permission = input("Please enter administrative password\n"
                                 ":")
        if admin_permission == user_database["admin"]:
            print("You may now register new user.")
            admin_reg_user()

    elif user_choice == "A":
        # read_task_database("tasks.txt", "r+") # manipulating task file
        add_task("tasks.txt", "r")  # taking details to add a task

    elif user_choice == "VA":

        view_all("tasks.txt", "r+")
        print_menu()
        # break

    elif user_choice == "VM":
        view_mine("tasks.txt", "r+")

    elif user_choice == "GTR":
        generate_task_report("tasks.txt", "r")

    elif user_choice == "GUR":
        generate_user_report("tasks.txt", "r")

    elif user_choice == "E":
        print("Exiting application")
        exit()

    else:
        print("The value that you have entered is invalid.")
        exit_application = input("Would you like to continue or quit?\n"
                                 "Continue\t\t\t\t\t\t C\n"
                                 "Quit\t\t\t\t\t\t\t Q\n"
                                 ":").upper()
        if exit_application == "C":
            print_menu()
        elif exit_application == "Q":
            print("Exiting application")
            exit()
