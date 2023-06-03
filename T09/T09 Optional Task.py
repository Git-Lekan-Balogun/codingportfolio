"""We're making a program for a department store to calculate the monthly wage for two different types of employees.
The employee in question is either a salesperson or a manager.
"""


print("Monthly wage calculator.")
employee_type = input("What employee are you?\n"
                      "Salesperson:\t\t[S]\n"
                      "\tManager:\t\t[M]\n")
employee_type = employee_type.upper()
# We start off by prompting the user to state their employee type.
# We've used \t to line up the menu options neatly or presentably. 

if employee_type == "S":
    print("Sales Staff.")
    gross_sales = float(input("What are you gross sales? £: "))
    commission = gross_sales * 0.08
    print(f"Your commission is currently calculated at £{commission}")
    per_month = float(input("How many months are we calculating for? "))
    base_wage = 2000 * per_month
    employee_wage = base_wage + commission
    print(f"Your wage is currently £{employee_wage}.")

elif employee_type == "M":
    print("Manager.")
    hours_worked = float(input("What are your worked hours? "))
    employee_wage = hours_worked * 40
    print(f"Your wage is currently £{employee_wage}.")
