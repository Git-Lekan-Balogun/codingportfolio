# amazon.py

import statistics

# import statistics module to use statistics.mean()

with open("input.txt", "r", encoding='utf-8-sig') as f:
    # I had to google this, but there is a few characters that are read to determine something about the file,
    # if you don't open through python with encoding 'utf-8-sig', the characters will display

    f_lines = f.readlines()
    # stores each line as an element in a list, this method keeps the \n characters, I suppose incase we wanted to
    # rewrite this to another file e.g. ['min:1,2,3,5,6\n', 'max:1,2,3,5,6\n', 'avg:1,2,3,5,6']

print(f_lines)


def min_max_avg(listed_string_integers):
    """This function takes in one argument, that is a variable that consists of list of elements in which the
    element is a sequence of numbers. The numbers are assumed to be string data type. Words such as "min", "max"
    and "avg" will be used to determine the functionality within the function.
    min returns the minimum integer or complex value in a formulated string
    max returns the maximum integer or comples value in a formulated string
    avg returns the average value in a formulated string"""

    writer = ""
    # this user defined function starts off by making an empty string that we will += all our values into

    for i in listed_string_integers:
        # for each element
        i = i.replace("\n", "")
        # remove \n character if it exists
        if "min" in i:
            # now we look for the "min" value if it exists, if it does:
            i = i.replace("min:", "")
            # get rid of it
            j = i.split(",")
            # separate the values as we want to convert them into integers
            new_list = []
            # new list to append values back into
            for k in j:
                k = int(k)
                # j is now a list, splitting our numbers by the commas that are already demarcating them
                # k is the number in j, as it stands it was a string but it is now being converted into an integer
                new_list.append(k)
                # we add the new int form into our empty list, and have essentially converted j into the same
            answer = min(new_list)
            # the answer is the smallest value in the list, which is 1, the above returns that result
            output = f"The minimum of {new_list} is {answer}."
            # this is our formatted string
            writer += output + "\n"
            # we're going to append the formatted string into our writer, our writer is a variable to write into a new
            # file, this process repeats by checking for variables "min" "max" and "avg" and functions differently
            # accordingly, we can even repeat the code block

        elif "max" in i:
            i = i.replace("max:", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = max(new_list)
            output = f"The maximum of {new_list} is {answer}."
            writer += output + "\n"

        elif "avg" in i:
            i = i.replace("avg:", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = (statistics.mean(new_list))
            output = f"The average of {new_list} is {answer}."
            writer += output + "\n"

    return writer


with open("output.txt", "w") as output1:
    output1.write(min_max_avg(f_lines))
    # with the functionality of the function it takes an argument, the argument is the readlines() variable of the file
    # with a compatible string format eg: "sum:int1,int2,int3,int4,int5,int6,int7etc








print(min_max_avg(f_lines))
