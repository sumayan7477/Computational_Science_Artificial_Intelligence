# Shipping cost calculator based on order value 

# Get the total order value from the user
order_value = float(input("Enter the total order value in €: "))

# Shipping rules
if order_value >= 100:
    # Free shipping for orders over 100€
    shipping_cost = 0
elif order_value >= 50:
    # 5€ shipping for orders between 50€ and 100€
    shipping_cost = 5
elif order_value >= 20:
    # 10€ shipping for orders between 20€ and 50€
    shipping_cost = 10
else:
    # 15€ shipping for orders under 20€
    shipping_cost = 15

# Display the calculated shipping cost
print("The shipping cost for your order is " + str(round(shipping_cost, 2))+"€.")

 
