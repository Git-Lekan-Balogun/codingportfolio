minefield = [["#", "-", "#", "-", "-"],  # 0 00 01 02 03 04
             ["-", "-", "-", "-", "-"],  # 1 10 11 12 13 14
             ["-", "-", "-", "-", "-"],  # 2 20 21 22 23 24
             ["-", "-", "-", "-", "-"],  # 3 30 31 32 33 34
             ["-", "-", "-", "-", "-"]]  # 4 49 41 42 43 44
             # ["-", "-", "-", "-", "-"]]

#             [["#", "-", "-", "-", "-"],  # 0 00 01 02 03 04
#              ["-", "#", "#", "-", "-"],  # 1 10 11 12 13 14
#              ["-", "-", "-", "-", "-"],  # 2 20 21 22 23 24
#              ["-", "-", "-", "-", "-"],  # 3 30 31 32 33 34
#              ["-", "-", "-", "-", "-"]]

# the above is an example minefield input

store_col = []  # [5, 5, 5, 5, 5] # we will append the values into the list, to make a dynamic minefield

dynamic_row = len(minefield)  # studies the length of the entire list, each item is a row so dynamic row
# stores the fact that there are 5 rows
for row in range(dynamic_row):  # for each row, study the length
    dynamic_col = len(minefield[row])  # iterates through the rows, keeps the current iteration as the indexer, so seeks
    # the length of each item in the nested list
    store_col.append(dynamic_col)  # append the values into our earlier list

minefield_copy = []  # we append the length of a list into this list to make a nested list
for i in store_col:  # for i, the length a row in minefield
    minefield_copy.append([0] * i)  # append [0] * length of row in minefield

counter_row = 0  # this is going to iterate each row
counter = 0  # this is going to iterate through each item in row
outer_boundary_max = len(minefield)  # 6
outer_boundary_min = outer_boundary_max - outer_boundary_max  # 0
# boundary_iteration_counter = boundary_min

store_coordinates = []

for row in minefield:  # each row in minefield
    inner_boundary_max = len(row)  # dynamic length, checks the row length, so changes accordingly
    inner_boundary_min = inner_boundary_max - inner_boundary_max
    inner_list = []
    for mine_spot in row:
        if counter == outer_boundary_max:
            counter_row += 1
            counter = 0
        coordinate_row = str(counter_row)
        coordinate = str(counter)
        complete_coordinates = coordinate_row + coordinate

        inner_list.append(complete_coordinates)

        counter += 1
    store_coordinates.append(inner_list)

map = []

# print(store_coordinates[0][4])
for row in store_coordinates:
    pairs = []
    for digit in row:
        digit = digit.split()
        for i in digit:
            i = int(i)
            pairs.append(i)
    map.append(pairs)

print(map)

for i in minefield:
    print()


        # digit = int(digit)
        # print(digit)




    # store_int_coordinates = []
    #
    # for pair in store_coordinates:
    #     pairs = []
    #     for i in pair:
    #         i = int(i)
    #         pairs.append([i])
    #     store_int_coordinates.append(pairs)
    #

    #
    # for row in minefield:  # each row in minefield
    #     inner_boundary_max = len(row)  # dynamic length, checks the row length, so changes accordingly
    #     inner_boundary_min = inner_boundary_max - inner_boundary_max
    #
    #     for mine_spot in row:
    #         if counter == outer_boundary_max:
    #             counter_row += 1
    #             counter = 0
    #
    #
    #
    #         counter += 1


    # print(minefield)
    # print(minefield_copy)
    # print(store_coordinates)
    # print(f" look here {store_int_coordinates}")


    # for i in store_int_coordinates:
    #     print(i[-1])

    # for i in store_int_coordinates:
    #     print(i)
"""
unfortunately i was never able to solve task 28, I even went as far as to create coordinate that would be the same
size as the minefield, but instead of blanks and mines, this field would instead have the index values. i could attempt
this again trying the enumerate function, but as i've tried for a few days I will leave this for a moment - I think
i've had a good attempt

my main issue is not knowing how to iterate through a list whilst tracking the current iteration's index 

when i come back for another attempt, i'll use the enumerate function to do what i've attempted with the += operator
set two enumerations
one counts the length of the mine field (x rows)
one counts the length of each row (x mines)

when the length of the mine row is exceeded, the length of the mine field will +1
eg:

    for mine_spot in row:
        if counter == outer_boundary_max: (this is len(minefield) ### note, inner_bonudary needs ot be made within the loop
            counter_row += 1
            counter = 0
        coordinate_row = str(counter_row)
        coordinate = str(counter)
        complete_coordinates = coordinate_row + coordinate

        inner_list.append(complete_coordinates)

        counter += 1
"""