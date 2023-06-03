# task3.py
# This task requires us to make an application that reads in the amount of time that the user
# has taken to complete a triathlon and then award them accordingly.

swimming_time = float(input("What was your elapsed time for Swimming exercise?\n"))
cycling_time = float(input("What was your elapsed time for Cycling exercise?\n"))
running_time = float(input("What was your elapsed time for Running exercise?\n"))

qualifying_time = swimming_time + cycling_time + running_time

if qualifying_time < 100:
    print(f"You have finished within qualifying time ({qualifying_time}). You have been awarded Provincial Colours.")
elif qualifying_time <= 105:
    print(f"You finished within 5 minutes of qualifying time ({qualifying_time}). You have been awarded Provincial Half"
          f"Colours.")
elif qualifying_time <= 110:
    print(f"You finished within 10 minutes of qualifying time ({qualifying_time}). You have been awarded Provincial"
          f"Scroll.")
elif qualifying_time > 110:
    print(f"You finished more than 10 minutes of qualifying time ({qualifying_time}). You have not been awarded "
          f"Better luck next time.")

"""
This task is similar to the previous,"""