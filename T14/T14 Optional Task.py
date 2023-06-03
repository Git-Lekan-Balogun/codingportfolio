# optional_task.py
# we're creating a program that will ask the user to enter a number less than or
# equal to 100, if they enter a number bigger than a 100, they will be prompted to
# enter a number until they accurately follow the instructions, once done our program
# will perform some calculations
#
# (check if it is even, if it is multiply it by 2 and print it, if it isn't multiply
# it by 3 and print it.

print("Enter a number less than or equal to 100 only!")
while True:
    what_number_could_it_be = int(input(""))
    # what number could it end up as?
    if what_number_could_it_be > 100:
        print("Enter a number less than or equal to 100 please.")
        # if the number is bigger than 100, we simply loop again. infinitely
        # just like an alternative try-except block

    elif what_number_could_it_be % 2 == 0:
        print(f"Your number is {what_number_could_it_be}"
              f" which is an even number, if we multiply that by 2, you get {what_number_could_it_be * 2}")
        exit()
        # the elif is connected to the if, so we've checked to see if the number is
        # bigger than 100, if it isn't we're going to check to see if its even
        # by modulo by 2. if it is even then we'll perform our doubling
    else:
        print(f"Your number is {what_number_could_it_be}"
              f" which is an odd number, if we multiply that by 3, you get {what_number_could_it_be * 3}")
        exit()
        # the only other outcome we care for is if the number is odd, if it is we
        # triple it, if our number isn't bigger than 100 or even, then it is going
        # to be smaller than 100, and odd.

