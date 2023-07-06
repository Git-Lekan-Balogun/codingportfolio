# Task 29 Task 1

# the goal of this application is to create a calculator for the user
# this calculator must be able to handle errors and be a robust program

# print("Hello, welcome to Calculator app."
#       "Select an option from the menu:")
#
# user_choice = input("Addition:\t\t\t\t\t\t[+]\n"
#                     "Subtraction:\t\t\t\t\t\t\t\t[-]\n"
#                     "Multiplication:\t\t\t\t\t\t\t[*]\n"
#                     "Division:\t\t\t\t\t\t\t[/]\n"
#                     "Modulus:\t\t\t\t\t\t[%]\n"
#                     "Power of:\t\t\t\t\t\t\t\t\t[P]\n").lower()

import math


def operator(x, operating, y):
    """
    :param x: First number, this should be set as variable which takes user input
    :param operating: This is the operator at hand, it set to recognise a particular character and act accordingly
    :param y: Second number, set to second variable taking a second user input
    :return: returns value created when x is operated on by y
    """

    if operating == "+":
        result_z = x + y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    elif operating == "-":
        result_z = x - y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    elif operating == "*":
        result_z = x * y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    elif operating == "/":
        result_z = x / y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    elif operating == "%":
        result_z = x % y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    elif operating == "p" or operating == "P":
        result_z = x ** y
        result_z_string = str(result_z)
        if result_z_string[-1] == "0":
            result_z = int(result_z)

    return result_z


def inc_value(x):
    if x == "+":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "-":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "*":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "/":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "%":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "p":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "P":
        pass
        # print(f"\"{x}\" is and invalid input, please enter an operator or option")
    elif x == "E":
        pass
    elif x == "e":
        pass
    else:
        print(f"\"{x}\" is an invalid input, please enter an operator or option")

        # if users_operator != "+" and "-" and "*" and "/" and "%" and "p":


def suffix_id(counter):
    counter += 1
    string_counter = str(counter)
    print(string_counter[-1])
    if 11 <= counter <= 20:
        suffix_identification = "th"
    elif string_counter[-1] == "1":
        suffix_identification = "st"
    elif string_counter[-1] == "2":
        suffix_identification = "nd"
    elif string_counter[-1] == "3":
        suffix_identification = "rd"
    elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
        suffix_identification = "th"

    return suffix_identification


def what_suffix(counter):
    while True:
        counter += 1
        string_counter = str(counter)
        print(string_counter[-1])
        if 11 <= counter <= 20:
            suffix_identification = "th"
        elif string_counter[-1] == "1":
            suffix_identification = "st"
        elif string_counter[-1] == "2":
            suffix_identification = "nd"
        elif string_counter[-1] == "3":
            suffix_identification = "rd"
        elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
            suffix_identification = "th"

        return suffix_identification


# calculater start
counter = 0

while True:
    counter += 1
    string_counter = str(counter)
    if 11 <= counter <= 20:
        suffix = "th"
    elif string_counter[-1] == "1":
        suffix = "st"
    elif string_counter[-1] == "2":
        suffix = "nd"
    elif string_counter[-1] == "3":
        suffix = "rd"
    elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
        suffix = "th"

    # 1st
    # 2nd
    # 3rd
    # 4th 5th 6th 7th 8th 9th 10th 11th 12th 13th

    while True:
        try:
            users_num_raw = (input(f"Enter your {counter}{suffix} number: "))  # entering the first number to work with
            users_num = float(users_num_raw)
            break
        except ValueError:
            print(f"Please enter workable input.\n"
                  f"\"{users_num_raw}\" can not be used.\n")

    string_num = str(users_num)
    if string_num[-1] == "0":
        users_num = int(users_num)
    print(users_num)
    # the input accepts float, which in turn accepts integers (integers don't accept floats), they are just returned
    # in float form, for user experience if we get an integer, let the user recieve an integer back
    # when we convert the input into a string, check the last digit, if it's a 0 this is a whole number, if it's a whole
    # number lets have back an integer

    while True:
        users_operator = input("Enter the operator, enter E to end:\n"
                               "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                               "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                               "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()
        # this is our operator options menu, when the user selects from an option, that operator is applied

        inc_value(users_operator)

        if users_operator == "e":
            print("Closing app.")
            break

        elif users_operator == "+":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

        elif users_operator == "-":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

        elif users_operator == "*":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

        elif users_operator == "/":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

        elif users_operator == "%":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

        elif users_operator == "P":
            print(users_num, users_operator)
            counter += 1
            string_counter = str(counter)

            if 11 <= counter <= 20:
                suffix = "th"
                print("but is it this")

            elif string_counter[-1] == "1":
                suffix = "st"

            elif string_counter[-1] == "2":
                suffix = "nd"
            elif string_counter[-1] == "3":
                suffix = "rd"
            elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                suffix = "th"
                print("cant be this")

            while True:
                try:
                    users_second_num_raw = input(f"Enter your {counter}{suffix} number: ")
                    users_second_num = float(users_second_num_raw)
                    break
                except ValueError:
                    print(f"Please enter workable input.\n"
                          f"\"{users_second_num_raw}\" can not be used.\n")

            string_second_num = str(users_second_num)
            if string_second_num[-1] == "0":
                users_second_num = int(users_second_num)

            users_result = operator(users_num, users_operator, users_second_num)
            print(f"{users_num} {users_operator} {users_second_num} = {users_result}\n")

            while True:
                users_operator = input("Enter the operator, enter E to end:\n"
                                       "Addition:\t\t\t\t\t\t[+], Subtraction:\t\t\t\t\t[-]\n"
                                       "Multiplication:\t\t\t\t\t[*], Division:\t\t\t\t\t\t[/]\n"
                                       "Modulus:\t\t\t\t\t\t[%], Power of:\t\t\t\t\t\t[P]\n").lower()

                inc_value(users_operator)

                if users_operator == "e":
                    if users_result is float:
                        print(f"Closing app. Last answer: {users_result}")
                    else:
                        print(f"Closing app. Last answer: {math.trunc(users_result)}")

                    break

                print(f"{users_result} {users_operator}")

                counter += 1
                string_counter = str(counter)

                if 11 <= counter <= 20:
                    suffix = "th"
                    print("how")

                elif string_counter[-1] == "1":
                    suffix = "st"

                elif string_counter[-1] == "2":
                    suffix = "nd"
                elif string_counter[-1] == "3":
                    suffix = "rd"
                elif string_counter[-1] == "4" or "5" or "6" or "7" or "8" or "9" or "0":
                    suffix = "th"
                    print("Why")

                users_continuant = float(input(f"Enter your {counter}{suffix} number: "))
                previous_result = users_result

                users_string_continuant = str(users_continuant)
                if users_string_continuant[-1] == "0":
                    users_continuant = int(users_continuant)

                users_result = operator(users_result, users_operator, users_continuant)

                print(f"{previous_result} {users_operator} {users_continuant} = {users_result}\n")

            break

    break
