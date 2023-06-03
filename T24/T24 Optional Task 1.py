# optional_task.py

import statistics

# this task is an extension of T24 Task 3, essentially we extend our program so that it becomes compatible with even
# more inputs, e.g. "sum" and "p90"

with open("input2.txt", "r") as formatted_integers_txt:
    fi_text = formatted_integers_txt.readlines()
    # we read and store our text file into


# BIDMAS

# process_a = fi_text[3].split()
# print(process_a)
# process_b = process_a[1].split(",")
# print(process_b)
# process_a = process_a[0].replace("p", "")
# print(process_a[1])
# process_a = int(process_a.replace(":", ""))
#
#
# print(len(fi_text[3]))


def percentile_process(read_lines_txt):
    # we're making a function that takes one argument
    # this argument is the readlines variable that has the txt file with the number sequences
    # this is specifically for any line that reads p followed by a number for example p60

    process_x = read_lines_txt.split()  # ['p90:', '1,2,3,4,5,6,7,8,9,10'] one list; 2 elements
    process_a = process_x[0].replace("p", "")  # 90:
    # store index 0 into variable and remove the p
    process_a = int(process_a.replace(":", ""))  # 90 <int>
    # remove the colon, and cast to integer
    process_b = process_x[1].split(",")  # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    # for the second part of the line, split by the comma
    process_c = [process_a, process_b]
    # list comprehension, form a list of our two results, the formatted number and the list of integers
    return process_c
    # returns these values list of int and list


def percentile_formula(percentile_number, listed_string_integers):
    # this is the second part to our two part function
    # this function takes a percentile number and a list of integers
    # you need to take the arguments in as percentile process[0], percentile process[1]
    result = (percentile_number / 100 * len(listed_string_integers))
    # the outcome we need is our (percentile number) e.g. 50 / 100 = 0.5, 0.5 * (length of listed string ints) e.g. 10
    # = 5
    if type(result) == float:
        result = round(result)
        return result
        # result is the index of the value we want


def min_max_avgplus(x):
    writer = ""
    for i in x:
        # TODO: note, initially i had my writer variable placed here and was very confused for when my
        #  results only appended in once but I carefully corrected by mistake
        i = i.replace("\n", "")
        if "min: " in i:
            i = i.replace("min: ", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = min(new_list)
            output = f"The minimum of {new_list} is {answer}."
            writer += output + "\n"

        elif "max: " in i:
            i = i.replace("max: ", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = max(new_list)
            output = f"The maximum of {new_list} is {answer}."
            writer += output + "\n"

        elif "avg: " in i:
            i = i.replace("avg: ", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = (statistics.mean(new_list))
            output = f"The average of {new_list} is {answer}."
            writer += output + "\n"

        elif "p" in i:
            percentile = percentile_process(i)
            # returns a list, 2 elements, a number[0] and a list[1]
            locate_index = percentile_formula(percentile[0], percentile[1])
            # use number[0] and list[1] as arguments for percentile formula

            answer = locate_index
            # print(i)
            # print(locate_index)
            # print(listed_numbers)

            suffice = str(percentile[0])
            # takes the first char of the number, converts it to the string, it will be from 0 to 9, depending on the
            # value our following if statements will change
            suffix_1 = (suffice[0])

            if suffix_1 == "0":
                suffix_1 = "th"
            elif suffix_1 == "1":
                suffix_1 = "st"
            elif suffix_1 == "2":
                suffix_1 = "nd"
            elif suffix_1 == "3":
                suffix_1 = "rd"
            elif suffix_1 == "4":
                suffix_1 = "th"
            elif suffix_1 == "5":
                suffix_1 = "th"
            elif suffix_1 == "6":
                suffix_1 = "th"
            elif suffix_1 == "7":
                suffix_1 = "th"
            elif suffix_1 == "8":
                suffix_1 = "th"
            elif suffix_1 == "9":
                suffix_1 = "th"
            # helps us create a dynamic suffix to our outcome
            string_number_sequence = i.split()
            string_number_sequence = string_number_sequence[1]  # list(string_number_sequence[1])
            string_number_sequence = string_number_sequence.split(",")
            int_number_sequence = []
            # converting list of string numbers to integer

            for string_number in string_number_sequence:
                int_number = int(string_number)
                int_number_sequence.append(int_number)

            output = f"The {percentile[0]}{suffix_1} percentile of {int_number_sequence} is {answer}."
            writer += output + "\n"

        elif "sum: " in i:
            i = i.replace("sum: ", "")
            j = i.split(",")
            new_list = []
            for k in j:
                k = int(k)
                new_list.append(k)
            answer = (sum(new_list))
            output = f"The sum of {new_list} is {answer}."
            writer += output + "\n"
            # num does what min avg and max do, excepts adds the numbers together

    return writer


with open("output2.txt", "w") as output:
    output.write(min_max_avgplus(fi_text))
    # with the functionality of the function it takes an argument, the argument is the readlines() variable of the file
    # with a compatible string format eg: "sum:int1,int2,int3,int4,int5,int6,int7etc

print(min_max_avgplus(fi_text))
