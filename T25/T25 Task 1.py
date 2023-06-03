# debugging.py

# for this task we need to debug the code so that it works

def print_values_of(dictionary):
    for key in dictionary:
        print(dictionary[key])  # the index value in "dictionary was "k" but it needs to be "key"


simpson_catch_phrases = {"lisa": "BAAAAAART!",
                         "bart": "Eat My Shorts!",
                         "marge": "Mmm~mmmmm",
                         "homer": "d'oh", # homer's phrase was 'd'oh' which cant interpret well
                         "maggie": "(Pacifier Suck)"
                         }

print_values_of(simpson_catch_phrases)

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

"""
the original code in question:

def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[k])

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd'oh', "maggie": " (Pacifier Suck)"}

print_values_of(simpson_catch_phrases, 'lisa', 'bart', 'homer')

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''


"""
