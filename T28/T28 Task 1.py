

minefield = [["#", "-", "-", "-", "-"],  # 0 00 01 02 03 04
             ["-", "-", "-", "-", "-"],  # 1 10 11 12 13 14
             ["-", "-", "-", "-", "-"],  # 2 20 21 22 23 24
             ["-", "-", "-", "-", "-"],  # 3 30 31 32 33 34
             ["-", "-", "-", "-", "-"]]  # 4 49 41 42 43 44

# the above is an example minefield input

store_col = []  # [5, 5, 5, 5, 5] # we will append the values into the list, to make a dynamic minefield

dynamic_row = len(minefield)  # studies the length of the entire list, each item is a row so dynamic row
# stores the fact that there are 5 rows
for row in range(dynamic_row): # for each row, study the length
    dynamic_col = len(minefield[row])  # iterates through the rows, keeps the current iteration as the indexer, so seeks
    # the length of each item in the nested list
    store_col.append(dynamic_col)  # append the values into our earlier list

minefield_copy = []  # we append the length of a list into this list to make a nested list
for i in store_col:  # for i, the length a row in minefield
    minefield_copy.append([0] * i)  # append [0] * length of row in minefield

counter = -1  # this is going to iterate through each item in row
counter_row = 0  # this is going to iterate each row
iterations = 0

for row in minefield:  # each row in minefield
    for mine_spot in row:  # each iteration in the row


        counter += 1
        if counter == 5:
            counter = 0
            counter_row += 1
        print(f"{counter_row}{counter}")


# print(minefield_copy)
# print(minefield[0][0])

# admittedly, i wasn't able to complete this task.
# my logic was to prevent the application from going out of bounds (index errors) by hard coding
# the application to not attempt to access a value of 5 or - 1, when the current value is 4 or 0 respectively
# unfortunately, with all my attempts my application doesn't += 1 the surrounding indexes around the current iteration

# this is either because
# 1) mine_spot doesn't have the same id as the current iteration
    # i can test this by printing both ids as the loop iterates to see if they match
    # if they don't match, mine_spot is minefield[x][x] will not trigger any count




