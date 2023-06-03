# courier.py
"""For this task we're going to calculate the cost of sending a parcel."""

# To begin with we've set current price variable to 0, because no options have been selected yet.
# This task simulates life strangely, because it assumes that Royal Mail are going to purchase this 'item' for you and
# sort of reimburses you back, but we will work with that.

current_cost = 0
print(f"Current Cost: £{current_cost}")
# Nothing has occurred yet.

package_price = int(input("What is the price of the package you're purchasing?\n"))
current_cost = current_cost + package_price
print(f"Current Cost: £{current_cost}")
# You have selected the perfume you're buying. Royal Mail purchased it. They are billing you.

distance_to_go = int(input("How far is the distance of the delivery (M)?\n"))
del_method = input("Enter the respective keys to select the following options.\n"
                   "Air £0.36 per mile [A] or Freight £0.25 per mile [F]?\n")
del_method = del_method.upper()

if del_method == "A":
    del_method = 0.36
    current_cost = current_cost + (distance_to_go * del_method)
elif del_method == "F":
    del_method = 0.25
    current_cost = current_cost + (distance_to_go * del_method)
print(f"Current Cost: £{current_cost}")
# Here we've stored our distance this is going. Royal Mail will charge 0.36 per mile for Air and 0.25 for freight.
# Air is faster so more expensive. To make this is even simpler we could save distance_to_go * del_method in it's own
# variable like price_given_distance = distance_to_go * del_method

insurance = input("Full insurance £50 [F] or Limited insurance £25 [L]?\n")
insurance = insurance.upper()
if insurance == "F":
    insurance = 50
    current_cost = current_cost + insurance

elif insurance == "L":
    insurance = 25
    current_cost = current_cost + insurance
print(f"Current Cost: £{current_cost}")
# From here on out it's simple, user picks an option. The cost of their option gets added to the current cost.
# Because I've taken a break from coding I made this vital mistake where I added all the previous values.
# So instead of something like current_cost = current_cost + insurance
# I had something silly like current_cost = current_cost + (del_method * distance) + Buyers_fee + insurance
# I had forgotten that when we assign current_cost to current_cost + insurance, the value of current cost has since
# then been updated with the history of additions.

# In short, I've added the variables back into the equation when they're already factored in. Messing up the formula.

gift_wrap = input("Is the item grift wrapped £15 [G] or standard packaging £0 [S]?\n")
gift_wrap = gift_wrap.upper()
if gift_wrap == "G":
    gift_wrap = 15
    current_cost = current_cost + gift_wrap
elif insurance == "S":
    gift_wrap = 0
    current_cost = current_cost + gift_wrap
print(f"Current Cost: £{current_cost}")

priority = input("Is the item priority £100 [P] or or standard delivery £20 [S]?")
priority = priority.upper()
if priority == "P":
    priority = 100
    current_cost = current_cost + priority
elif priority == "S":
    priority = 20
    current_cost = current_cost + priority
print(f"Current Cost: £{current_cost}")

print(f"The price of your item's delivery will be £{current_cost}, thank you for choosing Royal Mail.")
# And finish.


