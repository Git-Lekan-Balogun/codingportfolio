# loop_lists.py

# counter = 0
# fave_movies = ["SuperBad", "8 Mile", "Scott Pilgrim Vs. The World", "Pacific Rim", "Spiderman"]
# for i in fave_movies:
#     counter += 1
#     print(f"Movie {counter}: {i}")

# perhaps this is cheeky, the task wants me to manipulate the data in order to iterate over my list and display the
# following
# Movie: SuperBad
# Movie: 8 Mile
# Movie: Scott
# Pilgrim Vs. The World
# Movie: Pacific Rim
# Movie: Spiderman

# whilst I have achieved this, its hint/suggestion is to use the enumerate function


fave_movies = ["SuperBad", "8 Mile", "Scott Pilgrim Vs. The World", "Pacific Rim", "Spiderman"]
for index, element in enumerate(fave_movies, 1):
    print(f"Movie {index}: {element}")

# after a moment's research we can use the enumerate function
# to use the enumerate function whilst looping thorugh a list
# for = loop through total elements in the data structure: our list
# index = the variable for what represents our index of elements, this can be set to anything
# element = the item in index
# enumerate itself takes two arguments, the iterable and the start count
# we're enumerating through our fave movies list, and we want to start from 1