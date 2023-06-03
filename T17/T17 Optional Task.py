# optional_task.py
# we're making a program that determines if a user's string is a palindrome,
# a palindrome is sentence of word that is the same backwards, e.g. racecar, dad, level

users_palindrome = "level"
# users_palindrome = input("Enter a string and let's see if it's a palindrome or not:\n")


string_count = len(users_palindrome)
# string total is equal to len function's number, storing this in a variable gives us a dynamic number

# string_finish = string_count + 1
# last_index = string_count - 1
# the code above would be needed if we used
counting_up = -1
counting_down = string_count

users_palindrome_status = False
for i in users_palindrome:

    counting_up += 1
    counting_down -= 1

    # print(f"does {users_palindrome[counting_up]} match {users_palindrome[counting_down]}")

    if users_palindrome[counting_up] != users_palindrome[counting_down]:
        print(f"Your string '{users_palindrome}', is not a Palindrome")
        break
    else:
        users_palindrome_status = True

if users_palindrome_status:
    print(f"Your string {users_palindrome}, is a Palindrome.")

#
# else:
#     users_palindrome_status = False
#     # seem to have an issue with our program stepping out of the range of the string, but why is it doing that?
#
#     if users_palindrome_status:
#         print(f"Your string {users_palindrome}, is a Palindrome.")
#     elif not users_palindrome_status:
#         print(f"Your string {users_palindrome}, is not a Palindrome")
