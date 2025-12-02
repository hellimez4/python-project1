
#Simple Grocery Cart Checkout Write a program that:
# Has a predefined dictionary of groceries with prices.
# Lets the user “add” items by typing their names.
# For each valid item, asks for the quantity. Keeps adding to the cart until the user types "checkout".
# Displays a final bill: each item, quantity, subtotal, and total. Skills practiced: dictionaries,
# loops, input(), math operations, formatting, error handling. help me solve way
# steps  What We need to do
# Have a dictionary of groceries.
# User types item names to add.
# Ask for quantity.
# End with "checkout".
# Print each item, quantity, subtotal, and grand total.

groceries = {
    "apple": 1.00,
    "milk": 2.50,
    "turkey": 8.00,
    "eggs": 2.00
}

cart = {}

print("Available groceries:")
for item, price in groceries.items():
    print(f"- {item}: ${price}")

while True:
    item = input("Add item (or type 'checkout'): ").lower()

    if item == "checkout":
        break

    if item in groceries:
        qty = int(input("Quantity: "))
        cart[item] = cart.get(item, 0) + qty
        print("Added!")
    else:
        print("Item not found!")

# --- Final Bill ---
print("\n---- FINAL BILL ----")
total = 0

for item, qty in cart.items():
    price = groceries[item]
    subtotal = qty * price
    print(f"{item} x{qty} = ${subtotal}")
    total += subtotal

print("Total:", total)
print("-----------------------")
print(f"TOTAL = ${total:.2f}")

