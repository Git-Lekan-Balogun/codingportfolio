#details.py
# For this task we need to use the input command to get name, age, house number and streetname.
# And print this out on a single sentence containing all the details.

print("Please enter your, ")
name = input("Name: ")
age = input("Age: ")
house_no = input("House Number: ")
street_name = input("Street Name: ")

print(f"{name} is {age} years old and lives on {house_no} {street_name}. Thank you for inputting your details {name}.")