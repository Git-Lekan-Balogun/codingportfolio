import datetime

current_time = datetime.datetime.today()
time_deduction = datetime.timedelta(-0.1)
a_day_ahead = current_time + datetime.timedelta(1)
a_moment_ago = current_time - time_deduction

print(a_day_ahead)
print(a_moment_ago)
