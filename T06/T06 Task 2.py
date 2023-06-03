# shopping.py
product1 = input("Enter the name of this product: ")
product2 = input("Enter the name of this product: ")
product3 = input("Enter the name of this product: ")

product1_price = float(input(f"What is the price of {product1}: "))
product2_price = float(input(f"What is the price of {product2}: "))
product3_price = float(input(f"What is the price of {product3}: "))

product_price_total = product1_price + product2_price + product3_price
product_price_average = (product1_price + product2_price + product3_price) / 3

print(f"The total price of {product1}, {product2} & {product3} is {product_price_total}.\n"
      f"The average price of {product1}, {product2} & {product3} is {round(product_price_average)}.")
