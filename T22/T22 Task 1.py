# cafe.py
"""Follow these steps:  Imagine you are running a café. Create a new Python file in your folder called café.py.
Create a list called menu, which should contain at least 4 items in the café. Next, create a dictionary called
stock, which should contain the stock value for each item on your menu. ● Create another dictionary called price,
which should contain the prices for each item on your menu. Next, calculate the total stock worth in the café. You
will need to remember to loop through the appropriate dictionaries and lists to do this. Finally, print out the
result of your calculation. """
# this task is going to test our understanding of dictionaries

print("Laylay's coffee shop")
# storefront, or app front
menu = ["coffee", "tea", "toast", "milk"]
# items for sale

stock = {
    menu[0]: 37,
    menu[1]: 73,
    menu[2]: 50,
    menu[3]: 15
}
# stock is stored in a dictionary, I like this visual of having each key-value pair on a new line, including brackets
# interestingly, the keys are list indexes, that refer back to our menu

price = {
    menu[0]: 4.50,
    menu[1]: 2.50,
    menu[2]: 0.50,
    menu[3]: 1.50
}
# dictionary for prices works similarly to stock dictionary

incrementing = 0  # this is going +=1, we will use this to iterate
worth_total = 0  # using this to total each stock * price value

for i in stock.values():  # loop through our dictionary stock values, 37, 73, 50, 15..
    worth = i * price.get(menu[incrementing])  # the stock value is stock * price, i = stock, price.getmenu = price
    print(f"{menu[incrementing]}:\t\t\t£{price.get(menu[incrementing])}\t\t\t{stock.get(menu[incrementing])} "
          f"Units\t\t\t£{worth}") # string format, prints e.g. "coffee:		£4.5		37 Units		£166.5"

    incrementing += 1  # end of the loop, increase increments value so that it.. increments
    # incrementing is being used to cycle through the index of price and stock dictionaries
    worth_total += worth  # for each loop, add the value of the unit worth, we will use this to get a whole stock worth
print(f"\n£{worth_total} current stock worth.")
# TODO: redo this code using enumerate() as this method is more pythonic
