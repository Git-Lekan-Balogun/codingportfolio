# optional_task.py

abbreviations = {
    "LOL": "Laugh out loud",
    "TTYL": "Talk to you later",
    "DKM": "Don't kill me",
    "IMY/ILY": "I miss you/I love you",
    "UI/UX": "User interface/User experience",
    "OOP": "Object orientated programing"
}

users_string = input("Enter an abbreviation: ")
users_string_upped = users_string.upper()
if users_string_upped in abbreviations.keys():
    print(f"Abbreviation: {users_string_upped}\nDefinition:\t{abbreviations.get(users_string_upped)}")
else:
    print(f"The abbreviation {users_string} is not found in the dictionary.")
