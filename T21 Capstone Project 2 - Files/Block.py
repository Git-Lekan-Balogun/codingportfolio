while True:
    which_user = input("Who is the task assigned to?\n"
                       ":")
    if which_user not in username_profiles:
        print("The user does not exist, please contact admin to create user or try again")
        add_task_attempt = continue_prompt()
        continue_quit(add_task_attempt)

    elif which_user in username_profiles:
        assigned_user = which_user
        break

task_title = input("What is the name of the task?\n"
                   ":")
task_title = task_title.replace(",", "")
task_description = input("What does the task entail?\n"
                         ":")
task_description = task_description.replace(",", "-")
while True:
    current_time = datetime.datetime.today()

    task_due_day = int(input("Task Due (Day):\n"
                             ":"))
    task_due_month = int(input("Task Due (Month):\n"
                               ":"))
    task_due_year = int(input("Task Due (Year):\n"
                              ":"))

    task_due_date = datetime.date(task_due_year, task_due_month, task_due_day)
    verify_date = datetime.datetime(task_due_year, task_due_month, task_due_day, 0, 0, 0)

    task_due_date = task_due_date.strftime("%d %b %Y")
    # print(task_due_date)
    time_deduction = datetime.timedelta()
    a_day_ahead = current_time + datetime.timedelta(1)
    a_moment_ago = current_time - time_deduction

    # we use datetime.timedelta() to manipulate time like maths, 1 is equal to 24 hours, so e.g. 0.5 would be 12
    # time_deduction = 0 (or, now) if the task is set before now (or now), then that is qutie unfair
    # a_day_ahead = anything within 24 hours (for argument's sake) is set too soon

    if verify_date < a_moment_ago:  # you can't set a task due for date earlier than now
        print(f"The task due date: \"{verify_date}\", \"{verify_date.strftime('%d %b %Y')}\"\n"
              f"is set before the current time: \"{a_moment_ago}\", \"{a_moment_ago.strftime('%d %b %Y')}\"\n"
              f"Due date cannot be a past time")
        attempt_set_task = continue_prompt()
        continue_quit(attempt_set_task)

    elif verify_date < a_day_ahead:
        print(f"The task due date: \"{verify_date}\", \"{verify_date.strftime('%d %b %Y')}\"\n"
              f"is set too soon: \"{a_day_ahead}\", \"{a_day_ahead.strftime('%d %b %Y')}\"\n"
              f"Please allow at least more than a day to set due date.")
        attempt_set_task = continue_prompt()
        continue_quit(attempt_set_task)

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

with open("tasks.txt", "a+") as task_database:
    task_database.write(f"{taskline}")
print(f"Task has been written to {task_database}")
print_menu()
