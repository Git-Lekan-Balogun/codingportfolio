# while
# we're creating a program which calculates the average of numbers entered by a user

print("Enter a number, the program will stop if you enter '-1':\n")
# again, print statement is external to input command, so we don't get spammed

equation = 0
# this variable is set to 0, we're going to append the sums of our user's input, because
# we constantly want the total, and we're going to divide this by the total number of entries

counter = 0
# each loop = +1 total numbers, therefore 5 loops = 5 numbers
# we can divide our equation by our counter

while True:
    print(f"Current value: {equation}\n"
          f"Total numbers: {counter}")
    # we're kind enough to let the user track their progress in real time
    # however this can get spammy (especially the 'total numbers' print statement)

    users_num = int(input(""))
    # invisible input as instructions are above
    if users_num == -1:
        # if the user enters -1, we will call it quits.
        # I made the mistake of entering "-1" which is a numbered string and not a number
        # paying attention to detail in coding is essential as the slightest upset leads
        # to a different outcome

        print(f"The total of your numbers is {equation}, you entered a total of {counter} "
              f"numbers. So the average is {equation / counter}")
        break
    else:
        equation += users_num
        counter += 1
        # if users_num isn't -1, we're going to keep appending the value
        # appending with numbers is identical to addition (at least I have not identified a
        # difference)
