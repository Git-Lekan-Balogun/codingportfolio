# optional_task.py

# For this task we need to create to compilation errors, 1) a runtime error and a 2) logical error

# 1) runtime error

# users_num = int(input("Enter a number: "))
# if users_num == 5:
#     users_num = users_num - 5
# users_mystery_num = (users_num ** users_num) / users_num
#
# print(users_mystery_num)

# this was a round about way of creating a zero division error which is a run time error, our program eventually
# is forced to make some calculations that will later lead to it's own attempt to divide a number by 0

# 2) logical error

# users_num = int(input("Enter a number and we'll times that number by itself as many times as that number is.\n"))
# users_og_num = users_num
# counter = 0
# for i in range(0, users_num):
#     counter += 1
#     users_num = users_num * users_num
#
# print(users_num)
# print(counter)
# print(f"The number you entered is {users_og_num}, we've looped that {counter} times, and your result is {users_num}!")

# i really like this one I think it as very creative
# what we have here is a logical error because we get a number that is always far greater than the expected or desired
# if we enter 2 for example, we get 16
# this is because we enter the loop twice, on the first loop users_num is updated with 2 * 2, which is 4
# then it is updated again with 4 * 4, which is 16
# the desired outcome should be 4, because we're looking for exponent answers but instead we have a crazy looped
# algorithm:
# 2 = 16
# 3 = 6561
# 4 = 4294967296
# 5 = 23283064365386962890625
# 6 = 63340286662973277706162286946811886609896461828096
# 7 = 1487815647197611695910312681741273570332356717154798949898498305086387315423300999654757561928633305897036801.
# it would be interesting if there were some kind of sequence to these numbers or patterns, thought it is probably
# unlikely, however I'll leave that to a mathematician to venture
#
