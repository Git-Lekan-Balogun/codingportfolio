# optional_task.py

# This was a playful task that seems like it wanted to test us on a nested loop that wasn't a
# multiplication times tables, the concept of nested loops for times tables was interesting and
# it's an algorithm that would've been challenging to create from research or solo thought, however
# with the bootcamp they had already demonstrated it, so mimicking it would not be a challenge

# curiously enough, this task did not state to explicitly use a nested loop, but it was definitely
# a good opportunity to implement one

# the task:
#  Get the user to input a number and cast it to an int. Store it in a variable called num.
#  Now, if the number is bigger than 10, use a for loop to output it as many times as its value
#  For example, if a user enters 11, the number 11 will be printed out 11 times.
#  If the user enters anything less than or equal to 10, the program should output "Sorry, too small".

counter = 0
# this counter was made almost retrospectively, i.e. upon writing the code I had to go back and
# add in this counter, the counter has to exist outside the loop because the loop restarts it
# back to 0 if it is inside it
print("Input a number:")
while True:
    num = int(input(""))
    if num < 10:
        print("Sorry the number is too small. Try again.")
    else:
        for i in range(0, num):
            print(num)

            counter += 1
            print(f"Counter: {counter}")
            if counter == num:
                exit()
