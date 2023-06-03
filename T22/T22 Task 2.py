# hash.py

"""Follow these steps: Create a new Python file in your folder called hash.py  Create a dictionary called
countryMap, where the KEYS are the name of a country (i.e. a string), and the VALUE for each key is the name of that
country's capital city. ○ For example: countryMap = { 'UnitedKingdom': 'London', 'Sweden': 'Stockholm',
'Canada': 'Ottawa' } What does print(countryMap['Sweden']) return? """

country_Map = {
    "Nigeria": "abuja",
    "Sweden": "Stockholm",
    "United Kingdom": "London",
    "Japan": "Tokyo"
}

print(country_Map["Sweden"])
print(country_Map.get("Sweden"))
# when printing the above Key, we get its value; stockholm

print(id((country_Map["Sweden"])))
print(id(country_Map.get("Sweden")))
# printing the id shows the same identification so these methods and their outcome are identical

