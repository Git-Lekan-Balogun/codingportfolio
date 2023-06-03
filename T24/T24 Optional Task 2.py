# optional_task2.py
"""Create a new Python file in your folder called optional_task.py Write a program that will act as a calculator.
Create functions named add_num, subtract_num, multiply_num, and divide_num that asks the user to enter two numbers
and adds, subtracts, multiplies, or divides them, respectively. Print out the following menu and ask the user to
input a number that corresponds to the option they would like to choose: Option 1 - add Option 2 - subtract Option 3
- multiply Option 4 - divide If the user enters 1 call the add_num function If the user enters 2 call the
subtract_num function If the user enters 3 call the multiply_num function If the user enters 4 call the divide_num
function Make sure that the result of the calculation is printed out to the screen. """


def add_num(x, y):
    return x + y


def subtract_num(x, y):
    return x - y


def multiply_num(x, y):
    return x * y


def divide_num(x, y):
    return x / y


"""add
subtract
multiply
divide"""

print("Calculator application\n"
      "Enter a respective key to calculate equations:\n"
      "Addition:\t\t\t\t\tA\n"
      "Subtraction:\t\t\t\tS\n"
      "Multiplication:\t\t\t\tM\n"
      "Division:\t\t\t\t\tD\n"
      )
while True:
    user_menu = input("").upper()
    if user_menu == "A":
        x_value = float(input("Enter number:\n"))
        y_value = float(input("Enter second number:\n"))

        result = add_num(x_value, y_value)
        print(result)
        print("Do you need another equation?\n"
              "Yes:\t\t\t\t\tY\n"
              "No:\t\t\t\t\t\tN\n"
              )
        while True:
            another_equation = input("").upper()
            if another_equation == "Y":
                print("Calculator application\n"
                      "Enter a respective key to calculate equations:\n"
                      "Addition:\t\t\t\t\tA\n"
                      "Subtraction:\t\t\t\tS\n"
                      "Multiplication:\t\t\t\tM\n"
                      "Division:\t\t\t\t\tD\n"
                      )
                break
            elif another_equation == "N":
                break

    elif user_menu == "S":
        x_value = float(input("Enter number:\n"))
        y_value = float(input("Enter second number:\n"))

        result = subtract_num(x_value, y_value)
        print(result)
        print("Do you need another equation?\n"
              "Yes:\t\t\t\t\tY\n"
              "No:\t\t\t\t\t\tN\n"
              )
        while True:
            another_equation = input("").upper()
            if another_equation == "Y":
                print("Calculator application\n"
                      "Enter a respective key to calculate equations:\n"
                      "Addition:\t\t\t\t\tA\n"
                      "Subtraction:\t\t\t\tS\n"
                      "Multiplication:\t\t\t\tM\n"
                      "Division:\t\t\t\t\tD\n"
                      )
                break
            elif another_equation == "N":
                break

    elif user_menu == "M":
        x_value = float(input("Enter number:\n"))
        y_value = float(input("Enter second number:\n"))

        result = multiply_num(x_value, y_value)
        print(result)
        print("Do you need another equation?\n"
              "Yes:\t\t\t\t\tY\n"
              "No:\t\t\t\t\t\tN\n"
              )
        while True:
            another_equation = input("").upper()
            if another_equation == "Y":
                print("Calculator application\n"
                      "Enter a respective key to calculate equations:\n"
                      "Addition:\t\t\t\t\tA\n"
                      "Subtraction:\t\t\t\tS\n"
                      "Multiplication:\t\t\t\tM\n"
                      "Division:\t\t\t\t\tD\n"
                      )
                break
            elif another_equation == "N":
                break

    elif user_menu == "D":
        x_value = float(input("Enter number:\n"))
        y_value = float(input("Enter second number:\n"))

        result = divide_num(x_value, y_value)
        print(result)
        print("Do you need another equation?\n"
              "Yes:\t\t\t\t\tY\n"
              "No:\t\t\t\t\t\tN\n"
              )
        while True:
            another_equation = input("").upper()
            if another_equation == "Y":
                print("Calculator application\n"
                      "Enter a respective key to calculate equations:\n"
                      "Addition:\t\t\t\t\tA\n"
                      "Subtraction:\t\t\t\tS\n"
                      "Multiplication:\t\t\t\tM\n"
                      "Division:\t\t\t\t\tD\n"
                      )
                break
            elif another_equation == "N":
                break

    else:
        print("You have entered an incorrect value")

        while True:
            print("Continue?\n"
                  "Yes:\t\t\t\t\tY\n"
                  "No:\t\t\t\t\t\tN\n"
                  )
            user_continue = input("").upper()
            if user_continue == "Y":
                print("Calculator application\n"
                      "Enter a respective key to calculate equations:\n"
                      "Addition:\t\t\t\t\tA\n"
                      "Subtraction:\t\t\t\tS\n"
                      "Multiplication:\t\t\t\tM\n"
                      "Division:\t\t\t\t\tD\n"
                      )
                break
            elif user_continue == "N":
                quit()
