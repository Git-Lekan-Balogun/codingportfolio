# loop1000.py
# our goal to demonstrate our understanding of lists continues

"""
● Create a new Python file in this folder called loop1000.py.
● You are asked to print out all the numbers from 1 to 1000. Write 2 lines of
code in your file to print out all numbers from 1 to 1000.
"""
thousand_list = (list(range(0, 1001)))
for i in thousand_list:
    if i % 2 == 0:
        print(i)
