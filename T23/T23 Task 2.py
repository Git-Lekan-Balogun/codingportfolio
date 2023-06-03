# jokes.py
import random
# we've imported a module called random, it allows us to use a pseudo randomizer in our code

jokes = {
    1: "What do you call a fish with three eyes?\nFiiish",
    2: "A french man walks out of the bathroom, but forgets his perfume"
       "What does he say?\nEau de toilette!",
    3: "A duck walks into a bar and says to the bartender, 'I'd like to buy some peanuts.' The bartender says, "
       "'Sorry, don't sell peanuts.' The duck leaves. The next day, the duck returns and again says, 'I want to buy "
       "some peanuts.' The bartender replies, a bit gruffly this time, 'I already told you I don't sell peanuts.' The "
       "duck leaves. The next day, the duck comes in once again and yet again demands, 'I want to buy some peanuts!' "
       "The outraged bartender yells back, 'I told you, I don't sell peanuts! If you ask one more time, I'll nail you "
       "to the wall!' The duck leaves. The next day, the duck walks into the bar and before the bartender can say a "
       "word, the duck asks, 'Do you have any nails?' The bartender looks taken aback and says quietly, 'Sorry, "
       "don't have nails.' The duck asks, 'Well then, do you have any peanuts?'",
    4: "6 out of 7 dwarfs statistically aren't happy.",
    5: "Whats the best thing about Switzerland?\nI don't know, but their flag is a huge plus!",
    6: "I can't stand being in a wheelchair!"
}
# we've stored some jokes in our dictionary, and the key are numbers so they can be accessed by our random int function
num = random.randint(1, 6)
print(jokes.get(num))